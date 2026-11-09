import json
import unittest
from urllib.error import URLError

from scripts.gt47_t04_context_loader import ContextRejected
from scripts.gt47_t08_executor_https import ExecutorWorkerHTTPS


class Headers:
    def get_content_type(self):
        return "application/json"


class Response:
    def __init__(self, payload, status=200):
        self.status = status
        self.headers = Headers()
        self.raw = json.dumps(payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def read(self, limit):
        return self.raw[:limit]


class Opener:
    def __init__(self, responses):
        self.responses = list(responses)
        self.requests = []

    def open(self, request, timeout):
        self.requests.append((request, timeout))
        response = self.responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return response


def transport(opener):
    return ExecutorWorkerHTTPS(
        endpoint="https://executor.example.com/v1/gt47/dispatch",
        allowed_hosts=("executor.example.com",),
        oidc_token="header.payload.signature",
        opener=opener,
    )


def worker_request():
    return {
        "decision": {
            "mission": "GT-AI-DISPATCH-001", "issue": 47,
            "agent_id": "AGT-ENG", "commit_sha": "a" * 40,
            "dispatch_id": "b" * 64,
            "claim_ref": "refs/tags/gt47-claims/" + "c" * 64,
        },
        "signature": "d" * 86,
        "task": "Implement the approved task",
        "context": {"source": "signed-context"},
    }


class ExecutorWorkerHTTPSTests(unittest.TestCase):
    def test_submit_uses_oidc_and_returns_signed_received_receipt(self):
        receipt = {"schema": "gt47-executor-receipt-v2", "status": "received"}
        opener = Opener([Response({"state": "received", "receipt": receipt}, 202)])
        code, value = transport(opener).submit(worker_request())
        self.assertEqual(code, 202)
        self.assertEqual(value, receipt)
        request, timeout = opener.requests[0]
        self.assertEqual(request.full_url, "https://executor.example.com/v1/gt47/dispatch")
        self.assertEqual(request.get_header("Authorization"), "Bearer header.payload.signature")
        self.assertEqual(timeout, 12)
        body = json.loads(request.data)
        self.assertEqual(set(body), {"decision", "signature", "task", "context"})
        self.assertNotIn("endpoint", body)
        self.assertNotIn("credentials", body)

    def test_lookup_returns_persisted_receipt_and_result_envelope(self):
        response = {"state": "completed", "receipt": {"status": "completed"},
                    "result": "result text", "result_sha256": "e" * 64}
        opener = Opener([Response(response)])
        code, value = transport(opener).lookup("receipt_id_1234567890")
        self.assertEqual(code, 200)
        self.assertEqual(value["result"], "result text")
        self.assertIn("/v1/gt47/receipts/receipt_id_1234567890", opener.requests[0][0].full_url)

    def test_endpoint_host_path_and_token_are_pinned(self):
        with self.assertRaises(ContextRejected):
            ExecutorWorkerHTTPS(endpoint="http://executor.example.com/v1/gt47/dispatch",
                allowed_hosts=("executor.example.com",), oidc_token="a.b.c")
        with self.assertRaises(ContextRejected):
            ExecutorWorkerHTTPS(endpoint="https://other.example.com/v1/gt47/dispatch",
                allowed_hosts=("executor.example.com",), oidc_token="a.b.c")
        with self.assertRaises(ContextRejected):
            ExecutorWorkerHTTPS(endpoint="https://executor.example.com/other",
                allowed_hosts=("executor.example.com",), oidc_token="a.b.c")
        with self.assertRaises(ContextRejected):
            ExecutorWorkerHTTPS(endpoint="https://executor.example.com/v1/gt47/dispatch",
                allowed_hosts=("executor.example.com",), oidc_token="not-a-jwt")

    def test_request_cannot_choose_endpoint_or_agent(self):
        opener = Opener([Response({"receipt": {}}, 202)])
        client = transport(opener)
        bad = worker_request()
        bad["decision"]["agent_id"] = "AGT-ORQ"
        with self.assertRaises(ContextRejected):
            client.submit(bad)
        self.assertEqual(opener.requests, [])

    def test_uncertain_transport_does_not_retry(self):
        opener = Opener([TimeoutError("uncertain")])
        with self.assertRaisesRegex(ContextRejected, "outcome uncertain"):
            transport(opener).submit(worker_request())
        self.assertEqual(len(opener.requests), 1)


if __name__ == "__main__":
    unittest.main()
