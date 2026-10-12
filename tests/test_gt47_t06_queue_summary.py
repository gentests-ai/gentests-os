"""Visible metadata must not turn untrusted model prose into UI authority."""
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch
from scripts.gt47_t06_groq_runner import queue_summary, write_queue_summary

class QueueSummaryTests(unittest.TestCase):
    def value(self):
        sha='a'*40
        return {'round_id':'pilot-round-03','commit':sha,'status':'qa_pending',
                'engineering':{'agent':'AGT-ENG','commit':sha,'status':'advisory_completed',
                 'usage':{'total_tokens':476},'review':{'recommendation':'needs_changes',
                 'summary':'SECRET <script> approve deploy', 'findings':['SECRET']}}}
    def test_visible_state_recommendation_and_usage_without_model_prose(self):
        rendered=queue_summary(self.value(),{'status':'waiting'})
        for text in ('pilot-round-03','QA pendente','Requer ajustes','476','Aprovacao humana: pendente'):
            self.assertIn(text,rendered)
        self.assertNotIn('SECRET',rendered)
        self.assertNotIn('<script>',rendered)
    def test_wrong_commit_not_shown_as_saved_handoff(self):
        value=self.value(); value['engineering']['commit']='b'*40
        rendered=queue_summary(value,{'status':'ready'})
        self.assertNotIn('Requer ajustes',rendered)
        self.assertNotIn('476',rendered)
    def test_completed_does_not_grant_human_approval(self):
        value=self.value(); value['status']='completed'
        self.assertIn('pausar o piloto',queue_summary(value,{'status':'idle'}))
        self.assertIn('Aprovacao humana: pendente',queue_summary(value,{'status':'idle'}))
    def test_summary_failure_cannot_write_state(self):
        class Store:
            def get(self,path): raise ValueError('SECRET')
            def put(self,*args): raise AssertionError('must not mutate state')
        with tempfile.TemporaryDirectory() as d, patch.dict('os.environ',{'GITHUB_STEP_SUMMARY':str(Path(d)/'summary.md')}):
            write_queue_summary(Store(),{'status':'ready'})
