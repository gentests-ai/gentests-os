import sqlite3
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from scripts.gt_dispatch_two_stage_offline import execute, evidence

REQ={'demand_id':'SYN-ENG20-001','run_id':'run-0001','type':'synthetic_diagnostic',
     'objective':'analyze synthetic workflow','synthetic':True,'scope':'simulate:synthetic'}

class TwoStageTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.db=Path(self.temp.name)/'trace.sqlite'
        self.req=dict(REQ)

    def test_real_two_stage_handoff(self):
        r=execute(self.db,self.req)
        self.assertEqual(r['state'],'done')
        self.assertEqual(r['stages'],['AGT-ORQ','AGT-ENG'])
        self.assertEqual(r['result']['received_from'],'AGT-ORQ')
        proof=evidence(self.db,self.req['run_id'])
        self.assertEqual(proof['request']['state'],'done')
        self.assertEqual([s['status'] for s in proof['stages']],['done','done'])
        self.assertEqual(proof['stages'][1]['input_hash'], proof['stages'][0]['output_hash'])
        self.assertEqual(proof['stages'][1]['output']['received_from'],'AGT-ORQ')

    def test_duplicate_no_loop(self):
        execute(self.db,self.req)
        r=execute(self.db,self.req)
        self.assertEqual(r['reason'],'duplicate_run')
        self.assertEqual(len(evidence(self.db,'run-0001')['stages']),2)

    def test_run_id_conflict(self):
        execute(self.db,self.req)
        self.req['objective']='changed'
        self.assertEqual(execute(self.db,self.req)['reason'],'run_id_collision')

    def test_disallowed_operations(self):
        for change in ({'scope':'merge'}, {'scope':'contents:write'}, {'type':'publish'}, {'synthetic':False}):
            with self.subTest(change=change):
                self.assertEqual(execute(self.db,{**self.req,**change})['state'],'blocked')
        self.assertIsNone(evidence(self.db,'run-0001')['request'])

    def test_missing_extra_wrong_type(self):
        for changed in ({**self.req,'extra':True}, {k:v for k,v in self.req.items() if k!='run_id'},
                        {**self.req,'run_id':True}):
            with self.subTest(changed=changed):
                self.assertEqual(execute(self.db,changed)['state'],'blocked')

    def test_orq_failure_stops_eng(self):
        r=execute(self.db,self.req,fail_at='AGT-ORQ')
        self.assertEqual(r['state'],'uncertain')
        self.assertEqual([s['contract'] for s in evidence(self.db,'run-0001')['stages']],['AGT-ORQ'])
        self.assertEqual(execute(self.db,self.req)['reason'],'duplicate_run')

    def test_eng_failure_preserves_first(self):
        r=execute(self.db,self.req,fail_at='AGT-ENG')
        self.assertEqual(r['state'],'uncertain')
        p=evidence(self.db,'run-0001')
        self.assertEqual([s['status'] for s in p['stages']],['done','uncertain'])
        self.assertEqual(p['stages'][1]['input_hash'],p['stages'][0]['output_hash'])

    def test_invalid_failure_hook(self):
        self.assertEqual(execute(self.db,self.req,fail_at='AGT-QA')['reason'],'invalid_failure_hook')

    def test_unknown_run_evidence(self):
        p=evidence(self.db,'unknown')
        self.assertIsNone(p['request'])
        self.assertEqual(p['stages'],[])


    def _cli(self, text):
        fixture=Path(self.temp.name)/'cli-input.json'
        fixture.write_text(text,encoding='utf-8')
        return subprocess.run([sys.executable,'-m','scripts.gt_dispatch_two_stage_offline',
                               '--fixture',str(fixture),'--db',str(self.db)],
                              capture_output=True,text=True,timeout=15)

    def _assert_cli_rejected(self, payload):
        p=self._cli(payload)
        self.assertEqual(p.returncode,2,p.stderr)
        self.assertNotIn('Traceback',p.stderr)
        self.assertEqual(p.stderr,'')
        self.assertEqual(json.loads(p.stdout),
                         {'state':'blocked','reason':'invalid_fields','retry':False})
        # No handler, checkpoint, or SQLite file should be touched.
        self.assertFalse(self.db.exists())

    def test_qa11_cli_empty_array(self):
        self._assert_cli_rejected('[]')

    def test_qa11_cli_null(self):
        self._assert_cli_rejected('null')

    def test_qa11_cli_string(self):
        self._assert_cli_rejected('"invalid request"')

    def test_qa11_cli_valid_still_runs_two_stages(self):
        p=self._cli(json.dumps(self.req))
        self.assertEqual(p.returncode,0,p.stderr)
        self.assertEqual(p.stderr,'')
        data=json.loads(p.stdout)
        self.assertEqual(data['execution']['state'],'done')
        self.assertEqual(data['execution']['stages'],['AGT-ORQ','AGT-ENG'])
        self.assertEqual([st['status'] for st in data['evidence']['stages']],['done','done'])
        self.assertEqual(data['evidence']['stages'][0]['output_hash'],
                         data['evidence']['stages'][1]['input_hash'])

if __name__=='__main__': unittest.main()
