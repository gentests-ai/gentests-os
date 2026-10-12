import unittest
from scripts.gt47_t04_context_loader import ContextRejected
from scripts.gt47_t06_openai_smoke import invoke_smoke, MODEL, MAX_OUTPUT_TOKENS


class SmokeTests(unittest.TestCase):
    def test_bounded_payload_and_metadata(self):
        def transport(payload):
            self.assertEqual(payload["model"], MODEL)
            self.assertEqual(payload["max_output_tokens"], MAX_OUTPUT_TOKENS)
            self.assertIs(payload["store"], False)
            self.assertNotIn("tools", payload)
            return {"status": "completed", "model": MODEL,
                    "usage": {"input_tokens": 24, "output_tokens": 4},
                    "output": [{"type": "message"}]}
        result = invoke_smoke(api_key="fake-test-key", dispatch_id="a" * 64,
                              transport=transport)
        self.assertEqual(result["status"], "smoke_pass")
        self.assertFalse(result["agent_mission_executed"])

    def test_no_token(self):
        with self.assertRaises(ContextRejected):
            invoke_smoke(api_key="", dispatch_id="a" * 64)

    def test_rejects_wrong_model(self):
        with self.assertRaises(ContextRejected):
            invoke_smoke(api_key="fake", dispatch_id="a" * 64,
                transport=lambda _: {"status": "completed", "model": "other",
                    "usage": {"input_tokens": 1, "output_tokens": 1}, "output": []})

    def test_rejects_overrun(self):
        with self.assertRaises(ContextRejected):
            invoke_smoke(api_key="fake", dispatch_id="a" * 64,
                transport=lambda _: {"status": "completed", "model": MODEL,
                    "usage": {"input_tokens": 1, "output_tokens": 999}, "output": []})

    def test_rejects_tool_output(self):
        with self.assertRaises(ContextRejected):
            invoke_smoke(api_key="fake", dispatch_id="a" * 64,
                transport=lambda _: {"status": "completed", "model": MODEL,
                    "usage": {"input_tokens": 1, "output_tokens": 1},
                    "output": [{"type": "function_call"}]})


if __name__ == "__main__":
    unittest.main()
