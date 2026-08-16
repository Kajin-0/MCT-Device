#!/usr/bin/env python3
"""Round-49 synthetic operational traversal/self-test."""
from __future__ import annotations
import argparse,hashlib,json,sqlite3,tempfile
from datetime import datetime,timedelta,timezone
from pathlib import Path
from mct_provenance_store import PermissionDenied,ProvenanceStore,StateViolation,new_id
try:from validate_mct_provenance import V as R48
except Exception:R48=None
BASE=datetime(2026,8,16,23,30,0,tzinfo=timezone.utc)
def ts(m):return (BASE+timedelta(minutes=m)).isoformat().replace("+00:00","Z")
def dig(s):return hashlib.sha256(s.encode()).hexdigest()
def base(rt,m):return {"id":new_id(rt,ts(m)),"record_type":rt,"created_at":ts(m),"revision":1,"synthetic":True}
def mat(m,phy,parents,root,state,roles):
 r=base("material_node",m);r.update(physical_object_id=phy,parent_node_ids=parents,root_node_id=root or r["id"],state_time=ts(m),state_label=state,roles=roles,experimental_unit_id=None,terminal=False);return r
def cfg(m,label,sup=None):
 r=base("configuration",m);r.update(config_class="ROUND49_REFERENCE_STACK",version_label=label,status="ACTIVE",valid_from=ts(m),valid_to=None,supersedes_id=sup);return r
def cal(m,cid):
 r=base("calibration",m);r.update(configuration_id=cid,scope="synthetic reference chain",status="VALID",valid_from=ts(m),valid_to=ts(240));return r
def gate(m,code,node,cid,kid,refs,scope):
 r=base("gate_decision",m);r.update(gate_code=code,node_id=node,proposed_operation=f"ROUND49 synthetic {code}",evaluated_at=ts(m),prerequisite_record_ids=refs,prerequisite_assertions=[{"key":"ROUND49-PREREQUISITES","status":"PASS","evidence_record_ids":refs}],configuration_ids=[cid],calibration_ids=[kid],technical_status="PASS",material_status="PASS",decision="GO",release_scope=scope,reviewer_ids=["ACT-RELEASE"]);return r
def proc(m,cls,inp,out,cid,kid,mode="STATE_TRANSITION"):
 r=base("process_event",m);r.update(event_class=cls,procedure_ref=f"ROUND49-{cls}",input_node_ids=[inp],output_node_ids=[out] if isinstance(out,str) else out,configuration_ids=[cid],calibration_ids=[kid],started_at=ts(m),ended_at=ts(m+1),execution_status="VALID",irreversible=True,state_changing=True,lineage_mode=mode);return r
def meas(m,node,cid,kid,raw,fields,method):
 r=base("measurement",m);r.update(node_id=node,method_ref=method,configuration_ids=[cid],calibration_ids=[kid],acquired_at=ts(m),qc_status="PASS",result_fields=fields,raw_data_refs=[{"uri":raw["uri"],"sha256":raw["sha256"]}],analysis_ref="ROUND49-ANALYSIS");return r

def run(root:Path,require_r48=True):
 s=ProvenanceStore(root);checks=[]
 try:
  for a,r in {"ACT-ADMIN":"SYSTEM_ADMIN","ACT-PROCESS":"PROCESS_OWNER","ACT-METROLOGY":"METROLOGY_OWNER","ACT-DOE":"DOE_OWNER","ACT-MATERIAL":"MATERIAL_CONTROL","ACT-RELEASE":"RELEASE_AUTHORITY","ACT-INDEPENDENT":"INDEPENDENT_REVIEWER"}.items():s.actor(a,r,ts(0))
  c=cfg(1,"CFG-R49-A");s.append(c,"ACT-ADMIN");k=cal(2,c["id"]);s.append(k,"ACT-METROLOGY",[(c["id"],"configuration")])
  phy=new_id("physical_object",ts(3));rootn=mat(3,phy,[],None,"STAGE0-INPUT",["MATERIAL_CONTROL"]);s.append(rootn,"ACT-MATERIAL")
  # rollback injection
  rb=mat(3,new_id("physical_object",ts(3)),[rootn["id"]],rootn["id"],"ROLLBACK-PROBE",["ENGINEERING_ONLY"])
  try:s.batch([(rb,"ACT-MATERIAL",[(rootn["id"],"parent")]),(dict(rb),"ACT-MATERIAL",[(rootn["id"],"parent")])]);checks.append(("atomic-batch-rolls-back-on-failure",False))
  except sqlite3.DatabaseError:checks.append(("atomic-batch-rolls-back-on-failure",not s.exists(rb["id"])))
  gates=[]
  g0=gate(4,"G0",rootn["id"],c["id"],k["id"],[c["id"],k["id"]],"Stage-0");s.append(g0,"ACT-RELEASE",[(c["id"],"configuration"),(k["id"],"calibration")]);gates.append(g0["id"])
  bad=gate(4,"G0",rootn["id"],c["id"],k["id"],[c["id"]],"role probe");bad["id"]=new_id("gate_decision",ts(4))
  try:s.append(bad,"ACT-PROCESS",[(c["id"],"configuration")]);checks.append(("gate-role-policy-enforced",False))
  except PermissionDenied:checks.append(("gate-role-policy-enforced",True))
  grown=mat(6,phy,[rootn["id"]],rootn["id"],"GROWN",["FIT_POINT"]);pl=proc(5,"LPE",rootn["id"],grown["id"],c["id"],k["id"]);s.batch([(grown,"ACT-PROCESS",[(rootn["id"],"parent")]),(pl,"ACT-PROCESS",[(rootn["id"],"input"),(grown["id"],"output")])])
  g1=gate(7,"G1",grown["id"],c["id"],k["id"],[pl["id"]],"F2");s.append(g1,"ACT-RELEASE",[(pl["id"],"process")]);gates.append(g1["id"])
  g2=gate(8,"G2",grown["id"],c["id"],k["id"],[g1["id"]],"anneal");s.append(g2,"ACT-RELEASE",[(g1["id"],"gate")]);gates.append(g2["id"])
  ann=mat(10,phy,[grown["id"]],rootn["id"],"ANNEALED-N-LIKE",["FIT_POINT"]);pa=proc(9,"ANNEAL",grown["id"],ann["id"],c["id"],k["id"]);s.batch([(ann,"ACT-PROCESS",[(grown["id"],"parent")]),(pa,"ACT-PROCESS",[(grown["id"],"input"),(ann["id"],"output")])])
  g3=gate(11,"G3",ann["id"],c["id"],k["id"],[pa["id"]],"RIE");s.append(g3,"ACT-RELEASE",[(pa["id"],"process")]);gates.append(g3["id"])
  rie=mat(13,phy,[ann["id"]],rootn["id"],"RIE-WITNESS-QUALIFIED",["DETECTOR_BRIDGE"]);pr=proc(12,"RIE",ann["id"],rie["id"],c["id"],k["id"]);s.batch([(rie,"ACT-PROCESS",[(ann["id"],"parent")]),(pr,"ACT-PROCESS",[(ann["id"],"input"),(rie["id"],"output")])])
  g4=gate(14,"G4",rie["id"],c["id"],k["id"],[pr["id"]],"detector");s.append(g4,"ACT-RELEASE",[(pr["id"],"process")]);gates.append(g4["id"])
  det=mat(16,phy,[rie["id"]],rootn["id"],"BARE-DETECTOR",["DETECTOR_BRIDGE"]);pm=proc(15,"METALLIZATION",rie["id"],det["id"],c["id"],k["id"]);s.batch([(det,"ACT-PROCESS",[(rie["id"],"parent")]),(pm,"ACT-PROCESS",[(rie["id"],"input"),(det["id"],"output")])])
  g5=gate(17,"G5",det["id"],c["id"],k["id"],[pm["id"]],"P10-P13");s.append(g5,"ACT-RELEASE",[(pm["id"],"process")]);gates.append(g5["id"])
  p=root/"synthetic_detector_trace.txt";p.write_text("synthetic-only\nDstar=2.0e11\nnoise=24.5\n");raw=s.ingest(p,"ACT-METROLOGY",ts(18));checks.append(("raw-ingest-verified",s.verify_raw(raw["raw_id"])))
  mt=meas(19,det["id"],c["id"],k["id"],raw,["responsivity","noise_asd"],"ROUND49-P10-P12");s.append(mt,"ACT-METROLOGY",[(det["id"],"measured")])
  g6=gate(20,"G6",det["id"],c["id"],k["id"],[mt["id"]],"singulation");s.append(g6,"ACT-RELEASE",[(mt["id"],"measurement")]);gates.append(g6["id"])
  die=mat(22,new_id("physical_object",ts(22)),[det["id"]],rootn["id"],"SINGULATED-DIE",["DETECTOR_BRIDGE"]);arc=mat(22,new_id("physical_object",ts(22)),[det["id"]],rootn["id"],"ARCHIVE-SIBLING",["ARCHIVE"]);ps=proc(21,"SINGULATION",det["id"],[die["id"],arc["id"]],c["id"],k["id"],"SPLIT");s.batch([(die,"ACT-PROCESS",[(det["id"],"parent")]),(arc,"ACT-PROCESS",[(det["id"],"parent")]),(ps,"ACT-PROCESS",[(det["id"],"input"),(die["id"],"output"),(arc["id"],"output")])])
  rl=base("reserve_lock",23);rl.update(node_ids=[arc["id"]],purpose="synthetic FA reserve",locked_at=ts(23),release_trigger_key="FA-QUESTION-CLOSED",release_trigger_description="release after protected question closes");s.append(rl,"ACT-MATERIAL",[(arc["id"],"reserve")])
  bg=gate(24,"G7",arc["id"],c["id"],k["id"],[rl["id"]],"blocked reserve")
  try:s.append(bg,"ACT-RELEASE",[(rl["id"],"reserve")]);checks.append(("reserve-lock-blocks-go",False))
  except StateViolation:checks.append(("reserve-lock-blocks-go",True))
  rel=base("reserve_release",25);rel.update(reserve_lock_id=rl["id"],released_at=ts(25),trigger_key="FA-QUESTION-CLOSED",basis_record_ids=[g6["id"]],reviewer_ids=["ACT-MATERIAL","ACT-RELEASE"]);s.append(rel,"ACT-MATERIAL",[(rl["id"],"lock"),(g6["id"],"basis")])
  g7=gate(26,"G7",die["id"],c["id"],k["id"],[ps["id"]],"package");s.append(g7,"ACT-RELEASE",[(ps["id"],"process")]);gates.append(g7["id"])
  pkg=mat(28,die["physical_object_id"],[die["id"]],rootn["id"],"PACKAGED-DETECTOR",["HOLDOUT","DETECTOR_BRIDGE"]);pp=proc(27,"PACKAGE",die["id"],pkg["id"],c["id"],k["id"]);s.batch([(pkg,"ACT-PROCESS",[(die["id"],"parent")]),(pp,"ACT-PROCESS",[(die["id"],"input"),(pkg["id"],"output")])])
  h=base("holdout_lock",29);h.update(node_id=pkg["id"],campaign="F5-SYNTHETIC",protected_model_key="MODEL-R49-F5",protected_response_fields=["Dstar"],locked_at=ts(29),state="LOCKED",replacement_rule="execution-invalid only",model_freeze_id=None);s.append(h,"ACT-DOE",[(pkg["id"],"holdout")])
  hp=root/"synthetic_holdout_trace.txt";hp.write_text("synthetic holdout\nDstar=1.95e11\n");hr=s.ingest(hp,"ACT-METROLOGY",ts(30));mh=meas(31,pkg["id"],c["id"],k["id"],hr,["Dstar","temperature_qc"],"ROUND49-F5-HOLDOUT");s.append(mh,"ACT-METROLOGY",[(pkg["id"],"measured")]);s.seal(h["id"],mh["id"],"Dstar",1.95e11,"ACT-METROLOGY",ts(31))
  try:s.open_outcome(h["id"],mh["id"],["Dstar"],"MISSING","ACT-INDEPENDENT",ts(32));checks.append(("holdout-sealed-before-freeze",False))
  except StateViolation:checks.append(("holdout-sealed-before-freeze",True))
  try:s.open_outcome(h["id"],mh["id"],["Dstar"],"MISSING","ACT-PROCESS",ts(32));checks.append(("holdout-role-enforced",False))
  except PermissionDenied:checks.append(("holdout-role-enforced",True))
  f=base("model_freeze",33);f.update(model_key="MODEL-R49-F5",model_revision="R49.1",campaign="F5-SYNTHETIC",frozen_at=ts(33),training_measurement_ids=[mt["id"]],holdout_lock_ids=[h["id"]],model_digest_sha256=dig("MODEL-R49-F5-R49.1"));s.append(f,"ACT-DOE",[(mt["id"],"training"),(h["id"],"holdout")]);checks.append(("holdout-opens-after-freeze",s.open_outcome(h["id"],mh["id"],["Dstar"],f["id"],"ACT-INDEPENDENT",ts(34))=={"Dstar":1.95e11}))
  g8=gate(35,"G8",pkg["id"],c["id"],k["id"],[f["id"],h["id"]],"promotion");s.append(g8,"ACT-RELEASE",[(f["id"],"freeze"),(h["id"],"holdout")]);gates.append(g8["id"])
  states=["EMPIRICAL-REQUIRED","DESIGN-IDENTIFIED","DESIGN-RESOLUTION-VERIFIED","EMPIRICAL-PRELIMINARY","EMPIRICAL-VERIFIED","DETECTOR-BRIDGED","ALLOCATION-ELIGIBLE"];prev=None
  for i,(a,b) in enumerate(zip(states,states[1:])):
   q=base("evidence_promotion",36+i);verified=b in {"EMPIRICAL-VERIFIED","DETECTOR-BRIDGED","ALLOCATION-ELIGIBLE"};q.update(quantity_id="Q-R49-SYNTHETIC-DSTAR",from_state=a,to_state=b,promoted_at=ts(36+i),model_freeze_id=f["id"],holdout_lock_ids=[h["id"]],holdout_result="PASS" if verified else "NOT_REQUIRED",g8_gate_id=g8["id"],uncertainty_ref="UNC-R49" if b=="ALLOCATION-ELIGIBLE" else None,valid_range_ref="RANGE-R49" if b=="ALLOCATION-ELIGIBLE" else None,detector_bridge_ref=det["id"] if b in {"DETECTOR-BRIDGED","ALLOCATION-ELIGIBLE"} else None);deps=[(g8["id"],"g8"),(f["id"],"freeze"),(h["id"],"holdout")]+([(prev,"Prior")] if prev else []);s.append(q,"ACT-DOE",deps);prev=q["id"]
  checks.append(("g0-g8-nine-go",len(gates)==9 and all(s.get(x)["decision"]=="GO" for x in gates)))
  key=b"ROUND49-SYNTHETIC-KEY-NOT-FOR-PRODUCTION";sid=s.sign(g8["id"],"ACT-RELEASE","SYNTHETIC-KEY-01",key,ts(45));checks.extend([("signature-verifies",s.verify_sig(sid,key)),("signature-wrong-key-fails",not s.verify_sig(sid,b"wrong"))])
  for op,name in (("UPDATE records SET record_type='x' WHERE record_id=?","records-append-only-trigger"),("DELETE FROM records WHERE record_id=?","records-no-delete-trigger")):
   try:s.db.execute(op,(g8["id"],));s.db.commit();checks.append((name,False))
   except sqlite3.DatabaseError:s.db.rollback();checks.append((name,True))
  row=s.db.execute("SELECT object_path FROM raw_objects WHERE raw_id=?",(raw["raw_id"],)).fetchone();cas=root/row[0];orig=cas.read_bytes();cas.write_bytes(orig+b"TAMPER");checks.append(("raw-tamper-detected",not s.verify_raw(raw["raw_id"])));cas.write_bytes(orig);checks.append(("raw-restored-verifies",s.verify_raw(raw["raw_id"])))
  c2=cfg(60,"CFG-R49-B",c["id"]);s.append(c2,"ACT-ADMIN");inv=s.supersede(c["id"],c2["id"],ts(60),"ACT-ADMIN","synthetic replacement");checks.extend([("configuration-propagates-gate-invalidation",set(gates)<=set(inv)),("invalidated-gate-not-reusable",not s.gate_reusable(g8["id"]))])
  stale=gate(61,"G8",pkg["id"],c["id"],k["id"],[g8["id"]],"stale probe")
  try:s.append(stale,"ACT-RELEASE",[(g8["id"],"prior")]);checks.append(("superseded-config-blocks-new-use",False))
  except StateViolation:checks.append(("superseded-config-blocks-new-use",True))
  bundle=s.bundle("MCT-R49-SYNTHETIC-BUNDLE");r48status="SKIPPED";errs=None
  if R48 is None:
   if require_r48:raise RuntimeError("Round-48 validator import unavailable")
  else:errs=R48(bundle).run();r48status="PASS" if not errs else "FAIL";checks.append(("round48-semantic-validator-zero-errors",not errs))
  checks.append(("canonical-id-prefix",all(r["id"].startswith("MCT-") for r in bundle["records"])))
  bad=[n for n,x in checks if not x]
  if bad:raise AssertionError(", ".join(bad))
  out={"status":"PASS","checks_passed":len(checks),"checks_total":len(checks),"gates_go":len(gates),"gates_expected":9,"round48_validator_status":r48status,"round48_validator_errors":None if errs is None else len(errs),"summary":s.summary(),"bundle_record_count":len(bundle["records"]),"checks":[n for n,_ in checks]};(root/"round49_generated_bundle.json").write_text(json.dumps(bundle,indent=2)+"\n");(root/"round49_result.json").write_text(json.dumps(out,indent=2)+"\n");return out
 finally:s.close()

def main():
 ap=argparse.ArgumentParser();ap.add_argument("--workdir",type=Path);ap.add_argument("--allow-missing-round48-validator",action="store_true");a=ap.parse_args()
 if a.workdir:a.workdir.mkdir(parents=True,exist_ok=True);out=run(a.workdir,not a.allow_missing_round48_validator)
 else:
  with tempfile.TemporaryDirectory(prefix="mct-r49-") as d:out=run(Path(d),not a.allow_missing_round48_validator)
 print("ROUND49 REFERENCE SELF-TEST PASSED");print(json.dumps(out,indent=2,sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())
