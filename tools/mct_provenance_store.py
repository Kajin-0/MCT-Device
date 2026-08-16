#!/usr/bin/env python3
"""Round-49 stdlib-only SQLite provenance reference store."""
from __future__ import annotations
import hashlib,hmac,json,os,re,shutil,sqlite3,tempfile,uuid
from contextlib import contextmanager
from datetime import datetime,timezone
from pathlib import Path
from typing import Any,Iterable

SCHEMA_VERSION="mct-provenance-1.0.0"
PREFIX={"material_node":"MAT","process_event":"PROC","measurement":"MEAS","configuration":"CFG","calibration":"CAL","gate_decision":"GATE","holdout_lock":"HOLD","reserve_lock":"RSV","reserve_release":"REL","model_freeze":"MODEL","access_event":"ACC","deviation_rework":"DEV","evidence_promotion":"PROM","audit_event":"AUD","physical_object":"PHY","raw_object":"RAW","signature":"SIG"}
ID_RE=re.compile(r"^MCT-[A-Z]+-[0-9]{8}T[0-9]{6}Z-[A-F0-9]{12}$")
PROTECTED={"HOLDOUT","FIT_POINT","DETECTOR_BRIDGE"}
ROLES={"SYSTEM_ADMIN","PROCESS_OWNER","METROLOGY_OWNER","DOE_OWNER","MATERIAL_CONTROL","RELEASE_AUTHORITY","INDEPENDENT_REVIEWER"}
POLICY={
"material_node":{"SYSTEM_ADMIN","PROCESS_OWNER","MATERIAL_CONTROL"},"process_event":{"SYSTEM_ADMIN","PROCESS_OWNER"},"measurement":{"SYSTEM_ADMIN","METROLOGY_OWNER"},"configuration":{"SYSTEM_ADMIN","PROCESS_OWNER","METROLOGY_OWNER"},"calibration":{"SYSTEM_ADMIN","METROLOGY_OWNER"},"gate_decision":{"SYSTEM_ADMIN","RELEASE_AUTHORITY"},"holdout_lock":{"SYSTEM_ADMIN","DOE_OWNER","MATERIAL_CONTROL"},"reserve_lock":{"SYSTEM_ADMIN","MATERIAL_CONTROL"},"reserve_release":{"SYSTEM_ADMIN","MATERIAL_CONTROL","RELEASE_AUTHORITY"},"model_freeze":{"SYSTEM_ADMIN","DOE_OWNER"},"access_event":{"SYSTEM_ADMIN","METROLOGY_OWNER","INDEPENDENT_REVIEWER"},"deviation_rework":{"SYSTEM_ADMIN","PROCESS_OWNER","RELEASE_AUTHORITY"},"evidence_promotion":{"SYSTEM_ADMIN","DOE_OWNER","RELEASE_AUTHORITY"},"audit_event":ROLES}
class ProvenanceError(RuntimeError):pass
class PermissionDenied(ProvenanceError):pass
class StateViolation(ProvenanceError):pass

def now():return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")
def dt(x):return datetime.fromisoformat(x.replace("Z","+00:00"))
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def sha_bytes(x):return hashlib.sha256(x).hexdigest()
def sha_file(p):
 h=hashlib.sha256()
 with Path(p).open("rb") as f:
  for b in iter(lambda:f.read(1<<20),b""):h.update(b)
 return h.hexdigest()
def new_id(kind,at=None):
 if kind not in PREFIX:raise ValueError(kind)
 stamp=dt(at or now()).astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
 return f"MCT-{PREFIX[kind]}-{stamp}-{uuid.uuid4().hex[:12].upper()}"

class ProvenanceStore:
 def __init__(self,root):
  self.root=Path(root);self.root.mkdir(parents=True,exist_ok=True);self.obj=self.root/"objects/sha256";self.obj.mkdir(parents=True,exist_ok=True)
  self.db=sqlite3.connect(self.root/"provenance.sqlite3");self.db.row_factory=sqlite3.Row
  for p in ("PRAGMA foreign_keys=ON","PRAGMA journal_mode=WAL","PRAGMA synchronous=FULL"):self.db.execute(p)
  self._init()
 def close(self):self.db.close()
 def _init(self):
  self.db.executescript('''
CREATE TABLE IF NOT EXISTS actors(actor_id TEXT PRIMARY KEY,role TEXT NOT NULL,active INTEGER NOT NULL,created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS records(seq INTEGER PRIMARY KEY AUTOINCREMENT,record_id TEXT UNIQUE NOT NULL,record_type TEXT NOT NULL,created_at TEXT NOT NULL,actor_id TEXT NOT NULL REFERENCES actors(actor_id),payload_json TEXT NOT NULL,payload_sha256 TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS dependencies(record_id TEXT NOT NULL REFERENCES records(record_id),depends_on_id TEXT NOT NULL REFERENCES records(record_id),dependency_kind TEXT NOT NULL,PRIMARY KEY(record_id,depends_on_id,dependency_kind));
CREATE TABLE IF NOT EXISTS raw_objects(raw_id TEXT PRIMARY KEY,sha256 TEXT NOT NULL,size_bytes INTEGER NOT NULL,object_path TEXT NOT NULL,source_name TEXT NOT NULL,ingested_at TEXT NOT NULL,actor_id TEXT NOT NULL REFERENCES actors(actor_id));
CREATE TABLE IF NOT EXISTS sealed_outcomes(holdout_lock_id TEXT NOT NULL REFERENCES records(record_id),measurement_id TEXT NOT NULL REFERENCES records(record_id),field_name TEXT NOT NULL,value_json TEXT NOT NULL,stored_at TEXT NOT NULL,actor_id TEXT NOT NULL REFERENCES actors(actor_id),PRIMARY KEY(holdout_lock_id,measurement_id,field_name));
CREATE TABLE IF NOT EXISTS config_supersessions(old_config_id TEXT PRIMARY KEY REFERENCES records(record_id),new_config_id TEXT NOT NULL REFERENCES records(record_id),superseded_at TEXT NOT NULL,actor_id TEXT NOT NULL REFERENCES actors(actor_id),reason TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS gate_invalidations(gate_id TEXT NOT NULL REFERENCES records(record_id),config_id TEXT NOT NULL REFERENCES records(record_id),invalidated_at TEXT NOT NULL,actor_id TEXT NOT NULL REFERENCES actors(actor_id),reason TEXT NOT NULL,PRIMARY KEY(gate_id,config_id,invalidated_at));
CREATE TABLE IF NOT EXISTS signatures(signature_id TEXT PRIMARY KEY,target_record_id TEXT NOT NULL REFERENCES records(record_id),actor_id TEXT NOT NULL REFERENCES actors(actor_id),key_id TEXT NOT NULL,algorithm TEXT NOT NULL,signed_at TEXT NOT NULL,payload_digest TEXT NOT NULL,signature_hex TEXT NOT NULL);
''')
  for t in ("records","dependencies","raw_objects","sealed_outcomes","config_supersessions","gate_invalidations","signatures"):
   self.db.executescript(f"CREATE TRIGGER IF NOT EXISTS {t}_no_update BEFORE UPDATE ON {t} BEGIN SELECT RAISE(ABORT,'{t} append-only');END;CREATE TRIGGER IF NOT EXISTS {t}_no_delete BEFORE DELETE ON {t} BEGIN SELECT RAISE(ABORT,'{t} append-only');END;")
  self.db.commit()
 @contextmanager
 def tx(self):
  self.db.execute("BEGIN IMMEDIATE")
  try:yield
  except Exception:self.db.rollback();raise
  else:self.db.commit()
 def actor(self,aid,role,at=None):
  if role not in ROLES:raise ValueError(role)
  with self.tx():self.db.execute("INSERT INTO actors VALUES(?,?,1,?)",(aid,role,at or now()))
 def role(self,aid):
  r=self.db.execute("SELECT role,active FROM actors WHERE actor_id=?",(aid,)).fetchone()
  if not r or not r["active"]:raise PermissionDenied(aid)
  return r["role"]
 def require(self,aid,allowed):
  if self.role(aid) not in allowed:raise PermissionDenied(aid)
 def exists(self,rid):return self.db.execute("SELECT 1 FROM records WHERE record_id=?",(rid,)).fetchone() is not None
 def get(self,rid):
  r=self.db.execute("SELECT payload_json FROM records WHERE record_id=?",(rid,)).fetchone()
  if not r:raise StateViolation(f"missing {rid}")
  return json.loads(r[0])
 def rtime(self,p):
  return {"process_event":p.get("started_at"),"measurement":p.get("acquired_at"),"gate_decision":p.get("evaluated_at"),"access_event":p.get("accessed_at"),"reserve_release":p.get("released_at"),"model_freeze":p.get("frozen_at"),"evidence_promotion":p.get("promoted_at"),"deviation_rework":p.get("detected_at"),"audit_event":p.get("at")}.get(p.get("record_type"),p.get("created_at"))
 def config_active(self,cid,at):
  c=self.get(cid);x=dt(at)
  if c.get("record_type")!="configuration" or x<dt(c["valid_from"]) or (c.get("valid_to") and x>dt(c["valid_to"])) or c.get("status")=="RETIRED":return False
  s=self.db.execute("SELECT superseded_at FROM config_supersessions WHERE old_config_id=?",(cid,)).fetchone()
  return not(s and x>=dt(s[0]))
 def check_config(self,p):
  at=self.rtime(p)
  if not at:return
  cfg=p.get("configuration_ids",[])
  for cid in cfg:
   if not self.config_active(cid,at):raise StateViolation(f"stale configuration {cid}")
  for k in p.get("calibration_ids",[]):
   c=self.get(k);x=dt(at)
   if c.get("record_type")!="calibration" or c.get("status")!="VALID" or c.get("configuration_id") not in cfg or x<dt(c["valid_from"]) or (c.get("valid_to") and x>dt(c["valid_to"])):raise StateViolation(f"stale/mismatched calibration {k}")
 def reserve_locked(self,node,at):
  x=dt(at)
  for rr in self.db.execute("SELECT payload_json FROM records WHERE record_type='reserve_lock'"):
   lock=json.loads(rr[0])
   if node not in lock.get("node_ids",[]) or x<dt(lock["locked_at"]):continue
   ok=False
   for z in self.db.execute("SELECT payload_json FROM records WHERE record_type='reserve_release'"):
    rel=json.loads(z[0])
    if rel.get("reserve_lock_id")==lock["id"] and rel.get("trigger_key")==lock["release_trigger_key"] and dt(rel["released_at"])<=x:ok=True
   if not ok:return True
  return False
 def guard(self,p,aid):
  rt=p.get("record_type");self.require(aid,POLICY.get(rt,set()))
  if not ID_RE.fullmatch(p.get("id","")):raise StateViolation("noncanonical id")
  self.check_config(p)
  if rt=="gate_decision" and p.get("decision")=="GO":
   if p.get("technical_status")!="PASS" or p.get("material_status")!="PASS" or not p.get("prerequisite_assertions") or any(a.get("status")!="PASS" for a in p["prerequisite_assertions"]):raise StateViolation("illegal GO")
   refs=set(p.get("prerequisite_record_ids",[]))
   for a in p["prerequisite_assertions"]:refs.update(a.get("evidence_record_ids",[]))
   if any(not self.exists(r) for r in refs):raise StateViolation("missing GO prerequisite")
   if p.get("node_id") and self.reserve_locked(p["node_id"],p["evaluated_at"]):raise StateViolation("reserve locked")
  if rt=="reserve_release":
   lock=self.get(p["reserve_lock_id"])
   if p.get("trigger_key")!=lock.get("release_trigger_key") or dt(p["released_at"])<dt(lock["locked_at"]) or not p.get("basis_record_ids") or any(not self.exists(r) for r in p["basis_record_ids"]):raise StateViolation("invalid reserve release")
  if rt=="model_freeze":
   protected=set()
   for hid in p.get("holdout_lock_ids",[]):
    h=self.get(hid);node=h.get("node_id")
    for z in self.db.execute("SELECT payload_json FROM records WHERE record_type='measurement'"):
     m=json.loads(z[0])
     if m.get("node_id")==node and set(m.get("result_fields",[]))&set(h.get("protected_response_fields",[])):protected.add(m["id"])
   if protected&set(p.get("training_measurement_ids",[])):raise StateViolation("holdout training leak")
  if rt=="access_event":
   h=self.get(p["holdout_lock_id"]);fields=set(p.get("fields",[]));prot=set(h.get("protected_response_fields",[]))
   if p.get("access_type")=="QC" and fields&prot:raise StateViolation("QC outcome leak")
   if p.get("access_type")=="OUTCOME":
    self.require(aid,{"SYSTEM_ADMIN","INDEPENDENT_REVIEWER"});f=self.get(p.get("model_freeze_id"))
    if h["id"] not in f.get("holdout_lock_ids",[]) or dt(p["accessed_at"])<dt(f["frozen_at"]) or not fields or not fields<=prot:raise StateViolation("illegal outcome access")
  if rt=="deviation_rework" and p.get("state_changing"):
   ev=self.get(p.get("rework_process_event_id"));old=self.get(p["node_id"]);new=self.get(p.get("reassigned_role_node_id"))
   keep=set(old.get("roles",[]))&set(new.get("roles",[]))&PROTECTED
   if ev.get("event_class")!="REWORK" or new["id"] not in ev.get("output_node_ids",[]) or (keep and not p.get("equivalence_approval_id")):raise StateViolation("invalid rework role")
 def _insert(self,p,aid,deps):
  self.guard(p,aid);raw=canon(p)
  self.db.execute("INSERT INTO records(record_id,record_type,created_at,actor_id,payload_json,payload_sha256) VALUES(?,?,?,?,?,?)",(p["id"],p["record_type"],p["created_at"],aid,raw.decode(),sha_bytes(raw)))
  for dep,kind in deps:
   if not self.exists(dep):raise StateViolation(f"missing dependency {dep}")
   self.db.execute("INSERT INTO dependencies VALUES(?,?,?)",(p["id"],dep,kind))
  return p["id"]
 def append(self,p,aid,deps=()):
  with self.tx():return self._insert(p,aid,deps)
 def batch(self,items):
  out=[]
  with self.tx():
   for p,a,d in items:out.append(self._insert(p,a,d))
  return out
 def ingest(self,src,aid,at=None):
  self.require(aid,{"SYSTEM_ADMIN","METROLOGY_OWNER"});src=Path(src);digest=sha_file(src);d=self.obj/digest[:2];d.mkdir(parents=True,exist_ok=True);dest=d/digest
  if not dest.exists():
   fd,n=tempfile.mkstemp(prefix="ingest-",dir=d);os.close(fd);tmp=Path(n)
   try:
    shutil.copyfile(src,tmp)
    if sha_file(tmp)!=digest:raise StateViolation("ingest hash drift")
    os.replace(tmp,dest)
   finally:
    if tmp.exists():tmp.unlink()
  if sha_file(dest)!=digest:raise StateViolation("CAS hash mismatch")
  rid=new_id("raw_object",at)
  with self.tx():self.db.execute("INSERT INTO raw_objects VALUES(?,?,?,?,?,?,?)",(rid,digest,src.stat().st_size,str(dest.relative_to(self.root)),src.name,at or now(),aid))
  return {"raw_id":rid,"uri":f"cas://sha256/{digest}","sha256":digest,"size_bytes":src.stat().st_size}
 def verify_raw(self,rid):
  r=self.db.execute("SELECT sha256,object_path FROM raw_objects WHERE raw_id=?",(rid,)).fetchone()
  if not r:raise StateViolation(rid)
  p=self.root/r["object_path"];return p.is_file() and sha_file(p)==r["sha256"]
 def verify_all_raw(self):
  for r in self.db.execute("SELECT raw_id FROM raw_objects"):
   if not self.verify_raw(r[0]):raise StateViolation(f"raw integrity failure {r[0]}")
 def seal(self,hid,mid,field,value,aid,at=None):
  self.require(aid,{"SYSTEM_ADMIN","METROLOGY_OWNER"});h=self.get(hid);m=self.get(mid)
  if h.get("node_id")!=m.get("node_id") or field not in h.get("protected_response_fields",[]) or field not in m.get("result_fields",[]):raise StateViolation("invalid sealed field")
  with self.tx():self.db.execute("INSERT INTO sealed_outcomes VALUES(?,?,?,?,?,?)",(hid,mid,field,canon(value).decode(),at or now(),aid))
 def open_outcome(self,hid,mid,fields,fid,aid,at):
  self.require(aid,{"SYSTEM_ADMIN","INDEPENDENT_REVIEWER"})
  a={"id":new_id("access_event",at),"record_type":"access_event","created_at":at,"revision":1,"synthetic":True,"holdout_lock_id":hid,"access_type":"OUTCOME","accessed_at":at,"fields":fields,"model_freeze_id":fid}
  self.append(a,aid,[(hid,"holdout"),(fid,"model_freeze")])
  rows=self.db.execute("SELECT field_name,value_json FROM sealed_outcomes WHERE holdout_lock_id=? AND measurement_id=?",(hid,mid)).fetchall();v={r[0]:json.loads(r[1]) for r in rows if r[0] in fields}
  if set(v)!=set(fields):raise StateViolation("sealed fields incomplete")
  return v
 def supersede(self,old,new,at,aid,reason):
  self.require(aid,{"SYSTEM_ADMIN","PROCESS_OWNER","METROLOGY_OWNER"});n=self.get(new)
  if n.get("supersedes_id")!=old:raise StateViolation("supersedes_id mismatch")
  out=[]
  with self.tx():
   self.db.execute("INSERT INTO config_supersessions VALUES(?,?,?,?,?)",(old,new,at,aid,reason))
   for r in self.db.execute("SELECT payload_json FROM records WHERE record_type='gate_decision'"):
    g=json.loads(r[0])
    if g.get("decision")=="GO" and old in g.get("configuration_ids",[]):self.db.execute("INSERT INTO gate_invalidations VALUES(?,?,?,?,?)",(g["id"],old,at,aid,reason));out.append(g["id"])
  return sorted(out)
 def gate_reusable(self,gid):
  g=self.get(gid);return g.get("decision")=="GO" and self.db.execute("SELECT 1 FROM gate_invalidations WHERE gate_id=?",(gid,)).fetchone() is None
 def sign(self,target,aid,key_id,key,at=None):
  self.require(aid,{"SYSTEM_ADMIN","RELEASE_AUTHORITY","INDEPENDENT_REVIEWER"});r=self.db.execute("SELECT payload_sha256 FROM records WHERE record_id=?",(target,)).fetchone()
  if not r:raise StateViolation(target)
  t=at or now();msg=canon({"target_record_id":target,"payload_digest":r[0],"actor_id":aid,"key_id":key_id,"signed_at":t});sig=hmac.new(key,msg,hashlib.sha256).hexdigest();sid=new_id("signature",t)
  with self.tx():self.db.execute("INSERT INTO signatures VALUES(?,?,?,?,?,?,?,?)",(sid,target,aid,key_id,"HMAC-SHA256-REFERENCE",t,r[0],sig))
  return sid
 def verify_sig(self,sid,key):
  r=self.db.execute("SELECT * FROM signatures WHERE signature_id=?",(sid,)).fetchone();msg=canon({"target_record_id":r["target_record_id"],"payload_digest":r["payload_digest"],"actor_id":r["actor_id"],"key_id":r["key_id"],"signed_at":r["signed_at"]});return hmac.compare_digest(hmac.new(key,msg,hashlib.sha256).hexdigest(),r["signature_hex"])
 def bundle(self,bid,mode="SYNTHETIC"):
  self.verify_all_raw();records=[json.loads(r[0]) for r in self.db.execute("SELECT payload_json FROM records ORDER BY seq")]
  if mode=="SYNTHETIC" and any(r.get("synthetic") is not True for r in records):raise StateViolation("LAB record in synthetic bundle")
  return {"schema_version":SCHEMA_VERSION,"bundle_id":bid,"created_at":now(),"mode":mode,"records":records}
 def summary(self):
  c=lambda t:int(self.db.execute(f"SELECT count(*) FROM {t}").fetchone()[0])
  return {x:c(x) for x in ("records","raw_objects","sealed_outcomes","config_supersessions","gate_invalidations","signatures")}
