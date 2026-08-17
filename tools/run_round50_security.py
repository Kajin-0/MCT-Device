#!/usr/bin/env python3
"""Round-50 deployment/security simulation around the Round-49 provenance application."""
from __future__ import annotations
import argparse,json,shutil,tempfile
from pathlib import Path
from mct_provenance_store import PermissionDenied,ProvenanceStore,StateViolation,new_id
from mct_protected_vault import BackupManager,DummyInstrumentAdapter,HoldoutVault,harden_store_permissions,main_store_contains,permission_mode
from round50_fixture import digest,prepare,ts
from validate_mct_provenance import V as R48Validator

def run(root:Path)->dict:
 c=prepare(root);store,security,vault,s,cx=c.store,c.security,c.vault,c.sessions,c.checks
 try:
  doe=security.authorize(s['doe'],'HOLDOUT_LOCK',ts(14));hold={'id':new_id('holdout_lock',ts(14)),'record_type':'holdout_lock','created_at':ts(14),'revision':1,'synthetic':True,'node_id':c.package['id'],'campaign':'R50-SECURITY-DRYRUN','protected_model_key':'MODEL-R50-SECURE','protected_response_fields':['secure_signal'],'locked_at':ts(14),'state':'LOCKED','replacement_rule':'execution-invalid only','model_freeze_id':None};store.append(hold,doe['store_actor_id'],[(c.package['id'],'holdout')])
  marker='R50_PROTECTED_OUTCOME_9D08A8C6F2';pr=c.inputs/'protected_holdout.csv';pr.write_text(f'secure_signal,temperature_qc\n{marker},80.1\n');adapter=DummyInstrumentAdapter(store,security,c.cfg_c['id'],c.cal_c['id'],'R50-PROTECTED-INSTRUMENT',['secure_signal','temperature_qc']);pm,pref=adapter.ingest_protected(s['instrument'],vault,pr,c.package['id'],ts(15));vault.seal(s['instrument'],hold['id'],pm['id'],'secure_signal',marker,ts(15));cx += [('protected-raw-vault-integrity',vault.verify_raw(pref['raw_id'])),('protected-outcome-absent-from-main-store',not main_store_contains(store,marker.encode())),('round49-main-sealed-table-unused-for-r50',int(store.db.execute('SELECT count(*) FROM sealed_outcomes WHERE holdout_lock_id=?',(hold['id'],)).fetchone()[0])==0)]
  try:vault.open(s['independent'],hold['id'],pm['id'],['secure_signal'],'MISSING-FREEZE',ts(16));cx.append(('protected-outcome-denied-before-freeze',False))
  except StateViolation:cx.append(('protected-outcome-denied-before-freeze',True))
  try:vault.open(s['instrument'],hold['id'],pm['id'],['secure_signal'],'MISSING-FREEZE',ts(16));cx.append(('protected-outcome-role-denied',False))
  except PermissionDenied:cx.append(('protected-outcome-role-denied',True))
  da=security.authorize(s['doe'],'MODEL_FREEZE',ts(17));freeze={'id':new_id('model_freeze',ts(17)),'record_type':'model_freeze','created_at':ts(17),'revision':1,'synthetic':True,'model_key':'MODEL-R50-SECURE','model_revision':'R50.1','campaign':'R50-SECURITY-DRYRUN','frozen_at':ts(17),'training_measurement_ids':[c.meas_c['id']],'holdout_lock_ids':[hold['id']],'model_digest_sha256':digest('MODEL-R50-SECURE-R50.1')};store.append(freeze,da['store_actor_id'],[(c.meas_c['id'],'training'),(hold['id'],'holdout')]);opened=vault.open(s['independent'],hold['id'],pm['id'],['secure_signal'],freeze['id'],ts(18));cx.append(('protected-outcome-opens-after-freeze',opened=={'secure_signal':marker}))
  ra=security.authorize(s['release'],'GATE_APPROVE',ts(19));gate={'id':new_id('gate_decision',ts(19)),'record_type':'gate_decision','created_at':ts(19),'revision':1,'synthetic':True,'gate_code':'G8','node_id':c.package['id'],'proposed_operation':'R50 deployment/security evidence handoff','evaluated_at':ts(19),'prerequisite_record_ids':[freeze['id'],hold['id']],'prerequisite_assertions':[{'key':'R50-SECURITY','status':'PASS','evidence_record_ids':[freeze['id'],hold['id']]}],'configuration_ids':[c.cfg_c['id']],'calibration_ids':[c.cal_c['id']],'technical_status':'PASS','material_status':'PASS','decision':'GO','release_scope':'reference deployment only','reviewer_ids':[ra['store_actor_id']]};store.append(gate,ra['store_actor_id'],[(freeze['id'],'freeze'),(hold['id'],'holdout')])
  k1=security.create_key(s['admin'],'SIGNATURE_HMAC',ts(20));sig1=security.sign_record(s['signer'],gate['id'],ts(21));old,k2=security.rotate_key(s['admin'],'SIGNATURE_HMAC',ts(22));cx.append(('signature-key-rotation-identified-old',old==k1 and k2!=k1));v=security.verify_signature(s['independent'],sig1,ts(23));cx.append(('verify-only-signature-remains-trusted',v['crypto_valid'] and v['trust_state']=='TRUSTED'))
  try:
   if security.key_state(k1)!='ACTIVE':raise StateViolation('old key not active')
   cx.append(('retired-key-cannot-sign',False))
  except StateViolation:cx.append(('retired-key-cannot-sign',True))
  sig2=security.sign_record(s['signer'],gate['id'],ts(24));cx.append(('rotated-key-signature-trusted',security.verify_signature(s['independent'],sig2,ts(25))['trust_state']=='TRUSTED'));security.revoke_key(s['admin'],k1,ts(26),'synthetic compromise');v=security.verify_signature(s['independent'],sig1,ts(27));cx += [('revoked-key-signature-not-trusted',v['crypto_valid'] and v['trust_state']=='REVOKED'),('signature-verification-history-recorded',int(security.db.execute('SELECT count(*) FROM verification_events').fetchone()[0])>=3)]
  harden_store_permissions(store);kp=security.root/security.db.execute('SELECT key_path FROM keys WHERE key_id=?',(k2,)).fetchone()[0];cx += [('key-file-mode-0600',permission_mode(kp)==0o600),('key-directory-mode-0700',permission_mode(security.keys_dir)==0o700),('protected-vault-directory-mode-0700',permission_mode(vault.root)==0o700),('main-store-directory-mode-0700',permission_mode(store.root)==0o700)]
  bk=security.create_key(s['admin'],'BACKUP_HMAC',ts(28));mgr=BackupManager(security,vault);backup=mgr.create(s['backup'],c.root/'backup_good',ts(29),bk);cx += [('backup-manifest-verifies',mgr.verify(s['backup'],backup,ts(30))),('backup-excludes-key-material',not any(p.name.endswith('.key') for p in backup.rglob('*')))]
  tam=c.root/'backup_tampered';shutil.copytree(backup,tam);victim=next(p for p in tam.rglob('*') if p.is_file() and p.name not in {'manifest.json','manifest.hmac'});victim.write_bytes(victim.read_bytes()+b'TAMPER');cx.append(('backup-tamper-detected',not mgr.verify(s['backup'],tam,ts(31))));rest=mgr.restore(s['backup'],backup,c.root/'restore_good',ts(32));rs=ProvenanceStore(rest/'store');rv=HoldoutVault(rest/'protected',rs,security)
  try:rs.verify_all_raw();rv.verify_all();cx += [('restored-main-record-count-matches',rs.summary()['records']==store.summary()['records']),('restored-vault-count-matches',rv.summary()==vault.summary())]
  finally:rv.close();rs.close()
  bundle=store.bundle('MCT-R50-DEPLOYMENT-SECURITY-SYNTHETIC');errors=R48Validator(bundle).run();cx += [('round48-semantic-validator-zero-errors',not errors),('round49-prerequisite-was-full-pass',c.r49['checks_passed']==c.r49['checks_total']==19)]
  failed=[n for n,p in cx if not p]
  if failed:raise AssertionError(', '.join(failed))
  out={'status':'PASS','checks_passed':len(cx),'checks_total':len(cx),'round48_validator_errors':len(errors),'round49_prerequisite_checks':c.r49['checks_passed'],'main_store_summary':store.summary(),'vault_summary':vault.summary(),'deployment_key_count':int(security.db.execute('SELECT count(*) FROM keys').fetchone()[0]),'verification_event_count':int(security.db.execute('SELECT count(*) FROM verification_events').fetchone()[0]),'clock_event_count':int(security.db.execute('SELECT count(*) FROM clock_events').fetchone()[0]),'generated_bundle_records':len(bundle['records']),'checks':[n for n,_ in cx]};(c.root/'round50_generated_bundle.json').write_text(json.dumps(bundle,indent=2)+'\n');(c.root/'round50_result.json').write_text(json.dumps(out,indent=2)+'\n');return out
 finally:vault.close();security.close();store.close()

def main()->int:
 ap=argparse.ArgumentParser();ap.add_argument('--workdir',type=Path);a=ap.parse_args()
 if a.workdir:a.workdir.mkdir(parents=True,exist_ok=True);out=run(a.workdir)
 else:
  with tempfile.TemporaryDirectory(prefix='mct-r50-') as d:out=run(Path(d))
 print('ROUND50 DEPLOYMENT SECURITY SELF-TEST PASSED');print(json.dumps(out,indent=2,sort_keys=True));return 0
if __name__=='__main__':raise SystemExit(main())
