import os
import tempfile
import unittest

from scripts.gt47_t04_context_loader import ContextRejected
from scripts.gt47_t06_claim_store import claim_dispatch
from tests.test_gt47_t06_dispatch_intent import fixture
from scripts.gt47_t06_dispatch_intent import prepare_dispatch


class ClaimStoreTests(unittest.TestCase):
    def test_claim_then_replay_rejected_across_connections(self):
        ctx, request = fixture()
        intent = prepare_dispatch(context=ctx, request=request)
        with tempfile.TemporaryDirectory() as directory:
            db = os.path.join(directory, "claims.sqlite3")
            result = claim_dispatch(db, intent)
            self.assertEqual(result["status"], "claimed_offline")
            self.assertFalse(result["external_agent_invoked"])
            with self.assertRaises(ContextRejected):
                claim_dispatch(db, intent)
            request["nonce"] = "unique_nonce_0002"
            second = prepare_dispatch(context=ctx, request=request)
            self.assertNotEqual(result["dispatch_id"], claim_dispatch(db, second)["dispatch_id"])

    def test_rejects_forged_authorization(self):
        ctx, request = fixture()
        intent = prepare_dispatch(context=ctx, request=request)
        intent["authorization_granted"] = True
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ContextRejected):
                claim_dispatch(os.path.join(directory, "db"), intent)

    def test_fails_closed_on_store_error(self):
        ctx, request = fixture()
        intent = prepare_dispatch(context=ctx, request=request)
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ContextRejected):
                claim_dispatch(directory, intent)


if __name__ == "__main__":
    unittest.main()
