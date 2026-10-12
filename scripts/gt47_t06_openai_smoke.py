"""Bounded, opt-in OpenAI Responses API smoke adapter for GT47 T06.

Never imports mission comments into model instructions or writes to GitHub.
"""
from __future__ import annotations
import json
import re
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from scripts.gt47_t04_context_loader import ContextRejected

API_URL = "https://api.openai.com/v1/responses"
MODEL = "gpt-4.1-mini"
MAX_OUTPUT_TOKENS = 128
MAX_RESPONSE_BYTES = 32768


def invoke_smoke(*, api_key: str, dispatch_id: str, transport=None) -> dict:
    """One bounded model call; return metadata only, never model text."""
    if type(api_key) is not str or not api_key.strip():
        raise ContextRejected("API key required")
    if type(dispatch_id) is not str or not re.fullmatch(r"[0-9a-f]{64}", dispatch_id):
        raise ContextRejected("invalid dispatch id")
    payload = {
        "model": MODEL,
        "max_output_tokens": MAX_OUTPUT_TOKENS,
        "store": False,
        "instructions": "You are a test executor. Respond with exactly READY.",
        "input": "Health check: reply READY. Do not execute tools or take external actions.",
    }
    if transport is None:
        def transport(data):
            request = Request(API_URL, data=json.dumps(data).encode("utf-8"),
                headers={"Authorization": "Bearer " + api_key,
                         "Content-Type": "application/json"},
                method="POST")
            try:
                with urlopen(request, timeout=20) as response:
                    if response.status != 200:
                        raise ContextRejected("unexpected API response status")
                    raw = response.read(MAX_RESPONSE_BYTES + 1)
            except HTTPError as exc:
                raise ContextRejected(f"AI API HTTP status {exc.code}") from None
            except (URLError, TimeoutError, OSError):
                raise ContextRejected("AI API network failure") from None
            if len(raw) > MAX_RESPONSE_BYTES:
                raise ContextRejected("AI API response too large")
            try:
                return json.loads(raw.decode("utf-8"))
            except (ValueError, UnicodeError) as exc:
                raise ContextRejected("invalid AI API JSON") from exc
    response = transport(payload)
    if type(response) is not dict or response.get("status") != "completed" or response.get("model") != MODEL:
        raise ContextRejected("AI response incomplete or wrong model")
    usage = response.get("usage")
    if type(usage) is not dict:
        raise ContextRejected("missing token accounting")
    input_tokens = usage.get("input_tokens")
    output_tokens = usage.get("output_tokens")
    if (type(input_tokens) is not int or input_tokens < 0
            or type(output_tokens) is not int or not 0 <= output_tokens <= MAX_OUTPUT_TOKENS):
        raise ContextRejected("invalid token accounting")
    # No tool calls, no untrusted model output published.
    outputs = response.get("output")
    if type(outputs) is not list or any(
        type(item) is not dict or item.get("type") != "message" for item in outputs
    ):
        raise ContextRejected("unexpected AI output type")
    return {"status": "smoke_pass", "dispatch_id": dispatch_id,
            "model": MODEL, "input_tokens": input_tokens,
            "output_tokens": output_tokens, "github_write": False,
            "agent_mission_executed": False}
