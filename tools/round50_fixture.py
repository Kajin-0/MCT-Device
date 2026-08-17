#!/usr/bin/env python3
"""Round-50 synthetic deployment fixture/bootstrap helpers."""
from __future__ import annotations
import hashlib,json
from dataclasses import dataclass
from datetime import datetime,timedelta,timezone
from pathlib import Path

from mct_provenance_store import PermissionDenied,ProvenanceStore,StateViolation,new_id
from mct_deployment_control import DeploymentSecurity
from mct_protected_vault import DummyInstrumentAdapter,HoldoutVault
from run_round49_reference import run as run_round49

BASE=datetime(2026,8,17,1,0,0,tzinfo=timezone.utc)
def ts(m:int)->str:return (BASE+timedelta(minutes=m)).isoformat().replace('+00:00','Z')
def digest(text:str)->str:return hashlib.sha256(text.encode()).hexdigest()
def record(store,typ,pred):
 for row in store.db.execute('SELECT payload_json FROM records WHERE record_type=? ORDER BY seq',(typ,)):
  item=json.loads(row[0])
  if pred(item):return item
 raise StateViolation(f'missing {typ}')

@dataclass
class Context:
 root:Path;inputs:Path;store:ProvenanceStore;security:DeploymentSecurity;vault:HoldoutVault
 sessions:dict;checks:list;r49:dict;package:dict;cfg_c:dict;cal_c:dict;meas_c:dict

def prepare(root:Path)->Context:
 root=Path(root);root.mkdir(parents=True,exist_ok=True);baseline=root/'round49_baseline';inputs=root/'inputs';inputs.mkdir(parents=True,exist_ok=True)
 r49=run_round49(baseline,require_r48=True)
 if r49['status']!='PASS':raise AssertionError('Round-49 prerequisite failed')
 store=ProvenanceStore(baseline);security=DeploymentSecurity(root/'deployment',store);vault=HoldoutVault(root/'deployment/protected',store,security);checks=[]
 actor_roles={'ACT-R50-INSTRUMENT':'METROLOGY_OWNER','ACT-R50-CONFIG':'METROLOGY_OWNER','ACT-R50-RELEASE':'RELEASE_AUTHORITY','ACT-R50-INDEPENDENT':'INDEPENDENT_REVIEWER','ACT-R50-DOE':'DOE_OWNER','ACT-R50-SIGNER':'RELEASE_AUTHORITY','ACT-R50-BACKUP':'SYSTEM_ADMIN','ACT-R50-ADMIN':'SYSTEM_ADMIN'}
 for aid,role in actor_roles.items():store.actor(aid,role,ts(0))
 identities={'ID-R50-INSTRUMENT':('SERVICE_INSTRUMENT','ACT-R50-INSTRUMENT'),'ID-R50-CONFIG':('SERVICE_CONFIG','ACT-R50-CONFIG'),'ID-R50-RELEASE':('OP_RELEASE','ACT-R50-RELEASE'),'ID-R50-INDEPENDENT':('OP_INDEPENDENT','ACT-R50-INDEPENDENT'),'ID-R50-DOE':('OP_DOE','ACT-R50-DOE'),'ID-R50-SIGNER':('SERVICE_SIGNER','ACT-R50-SIGNER'),'ID-R50-BACKUP':('SERVICE_BACKUP','ACT-R50-BACKUP'),'ID-R50-ADMIN':('OP_ADMIN','ACT-R50-ADMIN')}
 for iid,(itype,aid) in identities.items():security.add_identity(iid,itype,aid,iid,ts(0))
 sessions={k:security.issue_session(i,ts(0),ts(180)) for k,i in {'instrument':'ID-R50-INSTRUMENT','config':'ID-R50-CONFIG','release':'ID-R50-RELEASE','independent':'ID-R50-INDEPENDENT','doe':'ID-R50-DOE','signer':'ID-R50-SIGNER','backup':'ID-R50-BACKUP','admin':'ID-R50-ADMIN'}.items()}
 try:security.authorize(sessions['instrument'],'GATE_APPROVE',ts(1));checks.append(('instrument-service-cannot-approve-gate',False))
 except PermissionDenied:checks.append(('instrument-service-cannot-approve-gate',True))
 try:security.authorize(sessions['release'],'INSTRUMENT_INGEST',ts(1));checks.append(('release-operator-cannot-ingest-instrument',False))
 except PermissionDenied:checks.append(('release-operator-cannot-ingest-instrument',True))
 disposable=security.issue_session('ID-R50-INSTRUMENT',ts(1),ts(20));security.revoke_session(disposable,ts(2),'synthetic revocation test')
 try:security.authorize(disposable,'INSTRUMENT_INGEST',ts(3));checks.append(('revoked-session-denied',False))
 except PermissionDenied:checks.append(('revoked-session-denied',True))
 checks.append(('clock-forward-accepted',security.accept_clock(sessions['admin'],ts(4),'SYSTEM_UTC')))
 try:security.accept_clock(sessions['admin'],ts(3),'SYSTEM_UTC');checks.append(('clock-backstep-rejected',False))
 except StateViolation:checks.append(('clock-backstep-rejected',True))
 checks.append(('clock-resumes-forward',security.accept_clock(sessions['admin'],ts(5),'SYSTEM_UTC')))
 package=record(store,'material_node',lambda r:r.get('state_label')=='PACKAGED-DETECTOR');cfg_b=record(store,'configuration',lambda r:r.get('version_label')=='CFG-R49-B')
 cal_b_spec=inputs/'calibration_b.json';cal_b_spec.write_text(json.dumps({'configuration_id':cfg_b['id'],'scope':'R50 dummy instrument B','valid_to':ts(150)}));cal_b=security.import_calibration(sessions['config'],cal_b_spec,ts(6))
 adapter_b=DummyInstrumentAdapter(store,security,cfg_b['id'],cal_b['id'],'R50-DUMMY-INSTRUMENT-B',['signal_v','temp_k']);raw_b=inputs/'dummy_b.csv';raw_b.write_text('signal_v,temp_k\n1.0e-6,80.0\n');meas_b=adapter_b.ingest(sessions['instrument'],raw_b,package['id'],ts(7));checks.append(('dummy-instrument-b-ingest',store.exists(meas_b['id'])))
 rel=security.authorize(sessions['release'],'GATE_APPROVE',ts(8));gate_b={'id':new_id('gate_decision',ts(8)),'record_type':'gate_decision','created_at':ts(8),'revision':1,'synthetic':True,'gate_code':'G5','node_id':package['id'],'proposed_operation':'R50 configuration-B deployment probe','evaluated_at':ts(8),'prerequisite_record_ids':[meas_b['id'],cal_b['id']],'prerequisite_assertions':[{'key':'R50-B-READY','status':'PASS','evidence_record_ids':[meas_b['id'],cal_b['id']]}],'configuration_ids':[cfg_b['id']],'calibration_ids':[cal_b['id']],'technical_status':'PASS','material_status':'PASS','decision':'GO','release_scope':'R50 deployment probe','reviewer_ids':[rel['store_actor_id']]};store.append(gate_b,rel['store_actor_id'],[(meas_b['id'],'measurement'),(cal_b['id'],'calibration')])
 cs=inputs/'configuration_c.json';cs.write_text(json.dumps({'config_class':'ROUND50-DUMMY-INSTRUMENT','version_label':'CFG-R50-C','supersedes_id':cfg_b['id']}));cfg_c=security.import_configuration(sessions['config'],cs,ts(9));ks=inputs/'calibration_c.json';ks.write_text(json.dumps({'configuration_id':cfg_c['id'],'scope':'R50 dummy instrument C','valid_to':ts(170)}));cal_c=security.import_calibration(sessions['config'],ks,ts(10));invalidated=security.supersede_configuration(sessions['config'],cfg_b['id'],cfg_c['id'],ts(11),'synthetic instrument replacement');checks.append(('config-supersession-invalidates-dependent-go',gate_b['id'] in invalidated and not store.gate_reusable(gate_b['id'])))
 n0=int(store.db.execute('SELECT count(*) FROM raw_objects').fetchone()[0])
 try:adapter_b.ingest(sessions['instrument'],raw_b,package['id'],ts(12));checks.append(('stale-adapter-rejected-before-copy',False))
 except StateViolation:checks.append(('stale-adapter-rejected-before-copy',int(store.db.execute('SELECT count(*) FROM raw_objects').fetchone()[0])==n0))
 adapter_c=DummyInstrumentAdapter(store,security,cfg_c['id'],cal_c['id'],'R50-DUMMY-INSTRUMENT-C',['signal_v','temp_k']);raw_c=inputs/'dummy_c.csv';raw_c.write_text('signal_v,temp_k\n1.1e-6,79.9\n');meas_c=adapter_c.ingest(sessions['instrument'],raw_c,package['id'],ts(13));checks.append(('replacement-adapter-ingest',store.exists(meas_c['id'])))
 return Context(root,inputs,store,security,vault,sessions,checks,r49,package,cfg_c,cal_c,meas_c)
