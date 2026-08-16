#!/usr/bin/env python3
"""MCT-Device Round-48 cross-record provenance validator; Python stdlib only."""
import argparse, copy, json, re, sys
from datetime import datetime
from pathlib import Path

SCHEMA_VERSION="mct-provenance-1.0.0"
EVIDENCE=["EMPIRICAL-REQUIRED","DESIGN-IDENTIFIED","DESIGN-RESOLUTION-VERIFIED","EMPIRICAL-PRELIMINARY","EMPIRICAL-VERIFIED","DETECTOR-BRIDGED","ALLOCATION-ELIGIBLE"]
PROTECTED={"HOLDOUT","FIT_POINT","DETECTOR_BRIDGE"}
SHA=re.compile(r"^[0-9a-f]{64}$")

REQ={
"material_node":"physical_object_id parent_node_ids root_node_id state_time state_label roles terminal",
"process_event":"event_class procedure_ref input_node_ids output_node_ids configuration_ids calibration_ids started_at ended_at execution_status irreversible state_changing lineage_mode",
"measurement":"node_id method_ref configuration_ids calibration_ids acquired_at qc_status result_fields raw_data_refs",
"configuration":"config_class version_label status valid_from valid_to supersedes_id",
"calibration":"configuration_id scope status valid_from valid_to",
"gate_decision":"gate_code node_id proposed_operation evaluated_at prerequisite_record_ids prerequisite_assertions configuration_ids calibration_ids technical_status material_status decision release_scope reviewer_ids",
"holdout_lock":"node_id campaign protected_model_key protected_response_fields locked_at state replacement_rule model_freeze_id",
"reserve_lock":"node_ids purpose locked_at release_trigger_key release_trigger_description",
"reserve_release":"reserve_lock_id released_at trigger_key basis_record_ids reviewer_ids",
"model_freeze":"model_key model_revision campaign frozen_at training_measurement_ids holdout_lock_ids model_digest_sha256",
"access_event":"holdout_lock_id access_type accessed_at fields model_freeze_id",
"deviation_rework":"node_id deviation_class detected_at disposition state_changing rework_process_event_id reassigned_role_node_id equivalence_approval_id",
"evidence_promotion":"quantity_id from_state to_state promoted_at model_freeze_id holdout_lock_ids holdout_result g8_gate_id uncertainty_ref valid_range_ref detector_bridge_ref",
"audit_event":"target_record_ids action actor_id role at digest_sha256",
}
REQ={k:set(v.split())|{"id","record_type","created_at","revision","synthetic"} for k,v in REQ.items()}
ENUM={
"process_event":{"event_class":{"LPE","ANNEAL","RIE","PASSIVATION","LITHOGRAPHY","METALLIZATION","SINGULATION","PACKAGE","REWORK","HANDLING","OTHER"},"execution_status":{"VALID","INVALID","DEVIATION"},"lineage_mode":{"STATE_TRANSITION","SPLIT"}},
"measurement":{"qc_status":{"PASS","HOLD","FAIL","INVALID"}},
"configuration":{"status":{"ACTIVE","SUPERSEDED","RETIRED"}},
"calibration":{"status":{"VALID","INVALIDATED","EXPIRED"}},
"gate_decision":{"gate_code":set("G"+str(i) for i in range(9)),"technical_status":{"PASS","HOLD","FAIL"},"material_status":{"PASS","HOLD","FAIL"},"decision":{"GO","HOLD","REWORK","STOP"}},
"holdout_lock":{"state":{"LOCKED","CONSUMED","RETIRED"}},
"access_event":{"access_type":{"QC","OUTCOME"}},
"deviation_rework":{"deviation_class":{"MEASUREMENT_INVALIDITY","HANDLING_DAMAGE","PROCESS_EXCURSION","TRUE_TREATMENT_RESPONSE","GENEALOGY_ERROR","CONFIGURATION_CHANGE","UNKNOWN"},"disposition":{"HOLD","REWORK","STOP","CONTINUE"}},
"evidence_promotion":{"from_state":set(EVIDENCE[:-1]),"to_state":set(EVIDENCE[1:]),"holdout_result":{"PASS","FAIL","INVALID","NOT_REQUIRED"}},
"audit_event":{"action":{"CREATE","REVIEW","APPROVE","INVALIDATE","SIGN"}},
}
REF={
"material_node":{"parent_node_ids":{"material_node"},"root_node_id":{"material_node"}},
"process_event":{"input_node_ids":{"material_node"},"output_node_ids":{"material_node"},"configuration_ids":{"configuration"},"calibration_ids":{"calibration"}},
"measurement":{"node_id":{"material_node"},"configuration_ids":{"configuration"},"calibration_ids":{"calibration"}},
"calibration":{"configuration_id":{"configuration"}},
"gate_decision":{"node_id":{"material_node"},"prerequisite_record_ids":None,"configuration_ids":{"configuration"},"calibration_ids":{"calibration"}},
"holdout_lock":{"node_id":{"material_node"},"model_freeze_id":{"model_freeze"}},
"reserve_lock":{"node_ids":{"material_node"}},
"reserve_release":{"reserve_lock_id":{"reserve_lock"},"basis_record_ids":None},
"model_freeze":{"training_measurement_ids":{"measurement"},"holdout_lock_ids":{"holdout_lock"}},
"access_event":{"holdout_lock_id":{"holdout_lock"},"model_freeze_id":{"model_freeze"}},
"deviation_rework":{"node_id":{"material_node"},"rework_process_event_id":{"process_event"},"reassigned_role_node_id":{"material_node"},"equivalence_approval_id":None},
"evidence_promotion":{"model_freeze_id":{"model_freeze"},"holdout_lock_ids":{"holdout_lock"},"g8_gate_id":{"gate_decision"}},
"audit_event":{"target_record_ids":None},
}

def t(v):
    return None if v is None else datetime.fromisoformat(v.replace("Z","+00:00"))
def vals(v):
    if v is None:return []
    return v if isinstance(v,list) else [v]

class V:
    def __init__(self,b):
        self.b=b; self.e=[]; self.rs=[]; self.by={}; self.bt={}
    def err(self,c,r,m): self.e.append((c,r,m))
    def time(self,v,r,f):
        try:return t(v)
        except Exception:self.err("E-TIME",r,f"{f} invalid RFC3339");return None
    def run(self):
        if not isinstance(self.b,dict):return [("E-BUNDLE","<bundle>","top level must be object")]
        if self.b.get("schema_version")!=SCHEMA_VERSION:self.err("E-SCHEMA","<bundle>","wrong schema_version")
        if self.b.get("mode") not in {"SYNTHETIC","LAB"}:self.err("E-MODE","<bundle>","bad mode")
        if not isinstance(self.b.get("records"),list) or not self.b["records"]:self.err("E-RECORDS","<bundle>","records must be nonempty array");return self.e
        self.rs=[r for r in self.b["records"] if isinstance(r,dict)]
        seen=set()
        for r in self.rs:
            rid=r.get("id","<missing>"); typ=r.get("record_type")
            if typ not in REQ:self.err("E-KIND",rid,f"unknown record_type {typ!r}");continue
            miss=REQ[typ]-set(r)
            if miss:self.err("E-REQUIRED",rid,"missing "+",".join(sorted(miss)))
            if rid in seen:self.err("E-ID-DUP",rid,"duplicate id")
            seen.add(rid)
            if not isinstance(r.get("revision"),int) or r.get("revision",0)<1:self.err("E-REV",rid,"revision must be >=1 integer")
            if not isinstance(r.get("synthetic"),bool):self.err("E-SYNTHETIC",rid,"synthetic must be boolean")
            self.time(r.get("created_at"),rid,"created_at")
            for f,a in ENUM.get(typ,{}).items():
                if f in r and r[f] not in a:self.err("E-ENUM",rid,f"{f}={r[f]!r} invalid")
            if typ=="measurement":
                for i,x in enumerate(r.get("raw_data_refs",[])):
                    if not isinstance(x,dict) or not x.get("uri"):self.err("E-DATA-REF",rid,f"raw_data_refs[{i}] missing uri")
                    if not isinstance(x,dict) or not SHA.fullmatch(x.get("sha256","")):self.err("E-DATA-HASH",rid,f"raw_data_refs[{i}] bad sha256")
            for f in ("model_digest_sha256","digest_sha256"):
                if f in r and not SHA.fullmatch(r.get(f,"")):self.err("E-DIGEST",rid,f"{f} bad sha256")
        for r in self.rs:
            if isinstance(r.get("id"),str) and r["id"] not in self.by:
                self.by[r["id"]]=r; self.bt.setdefault(r.get("record_type"),[]).append(r)
        if self.b.get("mode")=="SYNTHETIC":
            for r in self.rs:
                if r.get("synthetic") is not True:self.err("E-SYN-MODE",r.get("id"),"SYNTHETIC bundle requires synthetic=true")
        self.refs();self.material();self.events();self.configs();self.gates();self.reserves();self.holdouts();self.rework();self.promote()
        return sorted(self.e)

    def refs(self):
        for r in self.rs:
            for f,allowed in REF.get(r.get("record_type"),{}).items():
                for x in vals(r.get(f)):
                    if x is None:continue
                    z=self.by.get(x)
                    if not z:self.err("E-REF",r["id"],f"{f} missing {x}")
                    elif allowed and z.get("record_type") not in allowed:self.err("E-REF-KIND",r["id"],f"{f}->{x} wrong type")

    def material(self):
        m={r["id"]:r for r in self.bt.get("material_node",[])}
        g={}
        for rid,r in m.items():
            ps=r.get("parent_node_ids",[]);g[rid]=[p for p in ps if p in m]
            st=self.time(r.get("state_time"),rid,"state_time")
            if not ps and r.get("root_node_id")!=rid:self.err("E-ROOT",rid,"root must point to self")
            if ps and r.get("root_node_id")==rid:self.err("E-ROOT",rid,"nonroot points to self")
            for p in g[rid]:
                pt=self.time(m[p].get("state_time"),p,"state_time")
                if st and pt and st<pt:self.err("E-GENEALOGY-TIME",rid,f"precedes parent {p}")
        color={x:0 for x in m};stack=[]
        def dfs(x):
            color[x]=1;stack.append(x)
            for p in g[x]:
                if color[p]==1:self.err("E-GENEALOGY-CYCLE",x," -> ".join(stack[stack.index(p):]+[p]))
                elif color[p]==0:dfs(p)
            stack.pop();color[x]=2
        for x in m:
            if color[x]==0:dfs(x)
        def roots(x,path=frozenset()):
            if x in path:return set()
            if not g[x]:return {x}
            out=set()
            for p in g[x]:out|=roots(p,path|{x})
            return out
        for rid,r in m.items():
            rr=roots(rid)
            if len(rr)==1 and r.get("root_node_id") not in rr:self.err("E-ROOT-CONSISTENCY",rid,f"declared {r.get('root_node_id')} actual {next(iter(rr))}")
            if len(rr)>1:self.err("E-MULTIROOT",rid,f"multiple roots {sorted(rr)}")

    def events(self):
        m={r["id"]:r for r in self.bt.get("material_node",[])}
        for r in self.bt.get("process_event",[]):
            rid=r["id"];a=self.time(r.get("started_at"),rid,"started_at");b=self.time(r.get("ended_at"),rid,"ended_at")
            if a and b and b<a:self.err("E-EVENT-TIME",rid,"end before start")
            ins=[x for x in r.get("input_node_ids",[]) if x in m];outs=[x for x in r.get("output_node_ids",[]) if x in m]
            if r.get("lineage_mode")=="STATE_TRANSITION":
                if len(ins)!=1 or len(outs)!=1:self.err("E-LINEAGE-MODE",rid,"STATE_TRANSITION requires 1 input/1 output")
                elif m[ins[0]].get("physical_object_id")!=m[outs[0]].get("physical_object_id"):self.err("E-PHYSICAL-IDENTITY",rid,"state transition changed physical_object_id")
            if r.get("lineage_mode")=="SPLIT":
                if len(ins)!=1 or len(outs)<2:self.err("E-LINEAGE-MODE",rid,"SPLIT requires 1 input/>=2 outputs")
                elif len({m[x].get("physical_object_id") for x in outs})!=len(outs):self.err("E-SPLIT-IDENTITY",rid,"split output IDs not distinct")
            for o in outs:
                if set(m[o].get("parent_node_ids",[]))!=set(ins):self.err("E-EVENT-LINEAGE",rid,f"{o} parents != inputs")
                ot=self.time(m[o].get("state_time"),o,"state_time")
                if b and ot and ot<b:self.err("E-EVENT-OUTPUT-TIME",rid,f"{o} predates event end")

    def configs(self):
        cfg={r["id"]:r for r in self.bt.get("configuration",[])};cal={r["id"]:r for r in self.bt.get("calibration",[])}
        for r in list(cfg.values())+list(cal.values()):
            a=self.time(r.get("valid_from"),r["id"],"valid_from");b=self.time(r.get("valid_to"),r["id"],"valid_to")
            if a and b and b<a:self.err("E-VALIDITY",r["id"],"valid_to before valid_from")
        for r in cal.values():
            c=cfg.get(r.get("configuration_id"))
            if c:
                a=self.time(r.get("valid_from"),r["id"],"valid_from");b=self.time(r.get("valid_to"),r["id"],"valid_to")
                ca=self.time(c.get("valid_from"),c["id"],"valid_from");cb=self.time(c.get("valid_to"),c["id"],"valid_to")
                if a and ca and a<ca:self.err("E-CAL-CONFIG",r["id"],"cal starts before config")
                if b and cb and b>cb:self.err("E-CAL-CONFIG",r["id"],"cal extends past config")
        timed=[(r,"evaluated_at") for r in self.bt.get("gate_decision",[])]+[(r,"acquired_at") for r in self.bt.get("measurement",[])]+[(r,"started_at") for r in self.bt.get("process_event",[])]
        for r,f in timed:
            x=self.time(r.get(f),r["id"],f)
            if not x:continue
            for cid in r.get("configuration_ids",[]):
                c=cfg.get(cid)
                if c and ((self.time(c.get("valid_from"),cid,"valid_from") and x<self.time(c.get("valid_from"),cid,"valid_from")) or (self.time(c.get("valid_to"),cid,"valid_to") and x>self.time(c.get("valid_to"),cid,"valid_to"))):self.err("E-CONFIG-STALE",r["id"],f"{cid} invalid at use")
            for cid in r.get("calibration_ids",[]):
                c=cal.get(cid)
                if not c:continue
                a=self.time(c.get("valid_from"),cid,"valid_from");b=self.time(c.get("valid_to"),cid,"valid_to")
                if c.get("status")!="VALID" or (a and x<a) or (b and x>b):self.err("E-CAL-STALE",r["id"],f"{cid} invalid at use")
                if c.get("configuration_id") not in r.get("configuration_ids",[]):self.err("E-CAL-CONFIG-MISMATCH",r["id"],f"{cid} config not referenced")

    def gates(self):
        for r in self.bt.get("gate_decision",[]):
            ok=True;flat=set(r.get("prerequisite_record_ids",[]));aa=r.get("prerequisite_assertions",[])
            if not isinstance(aa,list) or not aa:ok=False;self.err("E-GATE-ASSERT",r["id"],"missing prerequisite assertions")
            for a in aa if isinstance(aa,list) else []:
                if not isinstance(a,dict) or a.get("status")!="PASS":ok=False
                for x in a.get("evidence_record_ids",[]) if isinstance(a,dict) else []:
                    if x not in self.by:self.err("E-GATE-ASSERT-REF",r["id"],f"missing {x}")
                    if x not in flat:self.err("E-GATE-ASSERT-FLAT",r["id"],f"{x} not in prerequisite_record_ids")
            ok=ok and r.get("technical_status")=="PASS" and r.get("material_status")=="PASS"
            if r.get("decision")=="GO" and not ok:self.err("E-GATE-GO",r["id"],"GO requires T/M/assertions PASS")

    def reserves(self):
        locks={r["id"]:r for r in self.bt.get("reserve_lock",[])};rels={}
        for r in self.bt.get("reserve_release",[]):
            l=locks.get(r.get("reserve_lock_id"));rels.setdefault(r.get("reserve_lock_id"),[]).append(r)
            if l and r.get("trigger_key")!=l.get("release_trigger_key"):self.err("E-RESERVE-TRIGGER",r["id"],"release trigger does not match lock")
            if not r.get("basis_record_ids"):self.err("E-RESERVE-BASIS",r["id"],"release missing basis")
            if l:
                a=self.time(l.get("locked_at"),l["id"],"locked_at");b=self.time(r.get("released_at"),r["id"],"released_at")
                if a and b and b<a:self.err("E-RESERVE-TIME",r["id"],"release before lock")
        for lid,l in locks.items():
            lt=self.time(l.get("locked_at"),lid,"locked_at")
            rt=min([self.time(x.get("released_at"),x["id"],"released_at") for x in rels.get(lid,[]) if self.time(x.get("released_at"),x["id"],"released_at")],default=None)
            for g in self.bt.get("gate_decision",[]):
                if g.get("decision")=="GO" and g.get("node_id") in set(l.get("node_ids",[])):
                    gt=self.time(g.get("evaluated_at"),g["id"],"evaluated_at")
                    if gt and lt and gt>=lt and (not rt or gt<rt):self.err("E-RESERVE-LOCK",g["id"],f"reserve {lid} still locked")

    def holdouts(self):
        h={r["id"]:r for r in self.bt.get("holdout_lock",[])};f={r["id"]:r for r in self.bt.get("model_freeze",[])};m={r["id"]:r for r in self.bt.get("measurement",[])}
        for x in h.values():
            n=self.by.get(x.get("node_id"))
            if n and "HOLDOUT" not in set(n.get("roles",[])):self.err("E-HOLDOUT-ROLE",x["id"],"locked node lacks HOLDOUT role")
        for z in f.values():
            hh=[h[x] for x in z.get("holdout_lock_ids",[]) if x in h]
            for mid in z.get("training_measurement_ids",[]):
                mm=m.get(mid)
                for x in hh:
                    if mm and mm.get("node_id")==x.get("node_id") and set(mm.get("result_fields",[]))&set(x.get("protected_response_fields",[])):self.err("E-HOLDOUT-TRAINING-LEAK",z["id"],f"{mid} contains protected holdout fields")
        for a in self.bt.get("access_event",[]):
            x=h.get(a.get("holdout_lock_id"))
            if not x:continue
            fields=set(a.get("fields",[]));prot=set(x.get("protected_response_fields",[]))
            if a.get("access_type")=="QC" and fields&prot:self.err("E-HOLDOUT-QC-LEAK",a["id"],"QC opened protected outcome")
            if a.get("access_type")=="OUTCOME":
                z=f.get(a.get("model_freeze_id"))
                if not z:self.err("E-HOLDOUT-NO-FREEZE",a["id"],"OUTCOME missing freeze");continue
                at=self.time(a.get("accessed_at"),a["id"],"accessed_at");ft=self.time(z.get("frozen_at"),z["id"],"frozen_at")
                if at and ft and at<ft:self.err("E-HOLDOUT-EARLY-OUTCOME",a["id"],"outcome opened before freeze")
                if a.get("holdout_lock_id") not in set(z.get("holdout_lock_ids",[])):self.err("E-HOLDOUT-WRONG-FREEZE",a["id"],"freeze does not protect holdout")
                if not fields<=prot:self.err("E-HOLDOUT-OUTCOME-FIELDS",a["id"],"outcome contains unprotected fields")

    def rework(self):
        ev={r["id"]:r for r in self.bt.get("process_event",[])}
        for r in self.bt.get("deviation_rework",[]):
            if r.get("disposition")!="REWORK":continue
            p=ev.get(r.get("rework_process_event_id"));n=self.by.get(r.get("reassigned_role_node_id"));o=self.by.get(r.get("node_id"))
            if not p or not n:self.err("E-REWORK-LINK",r["id"],"missing rework event/new node");continue
            if p.get("event_class")!="REWORK":self.err("E-REWORK-EVENT",r["id"],"event_class not REWORK")
            if n["id"] not in set(p.get("output_node_ids",[])):self.err("E-REWORK-OUTPUT",r["id"],"new node not event output")
            if r.get("state_changing") and o:
                keep=(set(o.get("roles",[]))&PROTECTED)&set(n.get("roles",[]))
                if keep and not r.get("equivalence_approval_id"):self.err("E-REWORK-PROTECTED-ROLE",r["id"],f"retained {sorted(keep)} without approval")

    def promote(self):
        g={r["id"]:r for r in self.bt.get("gate_decision",[])}
        for r in self.bt.get("evidence_promotion",[]):
            a,b=r.get("from_state"),r.get("to_state")
            if a in EVIDENCE and b in EVIDENCE and EVIDENCE.index(b)!=EVIDENCE.index(a)+1:self.err("E-PROMOTION-SKIP",r["id"],f"{a}->{b} skips state")
            x=g.get(r.get("g8_gate_id"))
            if x and (x.get("gate_code")!="G8" or x.get("decision")!="GO"):self.err("E-PROMOTION-G8",r["id"],"requires G8 GO")
            if b in {"EMPIRICAL-VERIFIED","DETECTOR-BRIDGED","ALLOCATION-ELIGIBLE"} and (r.get("holdout_result")!="PASS" or not r.get("holdout_lock_ids")):self.err("E-PROMOTION-HOLDOUT",r["id"],"verified+ requires PASS holdout")
            if b in {"DETECTOR-BRIDGED","ALLOCATION-ELIGIBLE"} and not r.get("detector_bridge_ref"):self.err("E-PROMOTION-BRIDGE",r["id"],"bridge required")
            if b=="ALLOCATION-ELIGIBLE" and (not r.get("uncertainty_ref") or not r.get("valid_range_ref")):self.err("E-PROMOTION-ALLOCATION",r["id"],"uncertainty/range required")

def load(p):
    with open(p,encoding="utf-8") as f:return json.load(f)
def validate(p):
    try:return V(load(p)).run()
    except Exception as e:return [("E-JSON",str(p),str(e))]

def mutate(b,ops):
    b=copy.deepcopy(b);by={r["id"]:r for r in b["records"]}
    for o in ops:
        if o["op"]=="set":by[o["record_id"]][o["field"]]=o.get("value")
        elif o["op"]=="append_record":b["records"].append(copy.deepcopy(o["record"]));by[o["record"]["id"]]=b["records"][-1]
        else:raise ValueError("unknown fixture op "+repr(o.get("op")))
    return b

def selftest(root):
    vd=root/"provenance/fixtures/valid";ip=root/"provenance/fixtures/invalid/round48_invalid_cases.json";fails=0;vc=ic=0
    valid={}
    for p in sorted(vd.glob("*.json")):
        b=load(p);valid[p.name]=b;e=V(b).run();vc+=1
        print(("PASS" if not e else "FAIL"),"valid",p)
        if e:fails+=1;[print(" ",x) for x in e]
    spec=load(ip);base=valid.get(Path(spec["base_fixture"]).name) or load((ip.parent/spec["base_fixture"]).resolve())
    for c in spec["cases"]:
        e=V(mutate(base,c["operations"])).run();ic+=1
        print(("PASS" if e else "FAIL"),"invalid",c["name"],f"({len(e)} error(s))")
        if not e:fails+=1
        else:[print(" ",x) for x in e[:5]]
    if fails:print("SELF-TEST FAILED",fails,file=sys.stderr);return 1
    print(f"SELF-TEST PASSED: {vc} valid + {ic} invalid case(s)");return 0

def main():
    ap=argparse.ArgumentParser();ap.add_argument("paths",nargs="*",type=Path);ap.add_argument("--self-test",action="store_true");ap.add_argument("--json",action="store_true");ap.add_argument("--repo-root",type=Path,default=Path(__file__).resolve().parents[1]);a=ap.parse_args()
    if a.self_test:return selftest(a.repo_root)
    if not a.paths:ap.error("provide paths or --self-test")
    out=[];ok=True
    for p in a.paths:
        e=validate(p);ok&=not e;out.append({"path":str(p),"valid":not e,"errors":[{"code":x[0],"record_id":x[1],"message":x[2]} for x in e]})
    if a.json:print(json.dumps(out,indent=2))
    else:
        for x in out:
            print(("PASS" if x["valid"] else "FAIL"),x["path"])
            for e in x["errors"]:print(" ",e["code"],f"[{e['record_id']}]",e["message"])
    return 0 if ok else 1
if __name__=="__main__":raise SystemExit(main())
