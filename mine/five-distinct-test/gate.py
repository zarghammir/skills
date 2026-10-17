"""five-distinct-test: a readiness gate for voice AI call-flow steps.

The rule: 5 DISTINCT real caller lines per step, ALL must land on the expected next step,
and ANY failure resets the streak to 0. Read-only: it starts calls, sends lines, ends calls.

USAGE:
  python3 gate.py gates.json      # run the gates in gates.json against your agent
  python3 gate.py --demo          # offline demo against a tiny built-in fake agent

gates.json:
  [
    { "name": "greeting_stays", "caller": "+15550000001", "setup": [],
      "variants": [ ["Hello?", "greeting"], ["Hi there.", "greeting"], ... 5 distinct ... ] },
    ...
  ]
  - caller:   caller number, if your agent treats known and unknown callers differently.
  - setup:    caller lines sent first, to walk the call to the step under test.
  - variants: [caller line, expected next step], at least 5 distinct lines.

Environment:
  VOICE_AGENT_URL    base URL of your agent's text test API (needed unless --demo)
  VOICE_AGENT_TOKEN  optional bearer token
  FALLBACK_STEP      optional: the step your agent falls back to when its model is down
"""
import json
import os
import sys
import urllib.request

DEFAULT_CALLER = "+15550000001"
FALLBACK_STEP = os.environ.get("FALLBACK_STEP")

# ---------------------------------------------------------------- ADAPTER
# Fill these three in for your platform. Each call returns plain Python values.
# The default version expects a simple JSON API:
#   POST {url}/start  {"caller": "..."}                 -> {"session_id": "..."}
#   POST {url}/say    {"session_id": "...", "text": ""} -> {"step": "...", "reply": "..."}
#   POST {url}/end    {"session_id": "..."}             -> anything

URL = os.environ.get("VOICE_AGENT_URL", "").rstrip("/")
TOKEN = os.environ.get("VOICE_AGENT_TOKEN")


def _post(path, body, timeout=60):
    req = urllib.request.Request(f"{URL}{path}", data=json.dumps(body).encode(), method="POST",
                                 headers={"Content-Type": "application/json",
                                          **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {})})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read()
    return json.loads(raw) if raw else {}


def start_call(caller):
    """Start a test conversation. Return a session id."""
    return _post("/start", {"caller": caller})["session_id"]


def say(session, text):
    """Send one caller line. Return (step the agent is now on, the agent's reply text)."""
    r = _post("/say", {"session_id": session, "text": text})
    return str(r.get("step")), (r.get("reply") or "").strip()


def end_call(session):
    try:
        _post("/end", {"session_id": session}, timeout=30)
    except Exception:
        pass
# ------------------------------------------------------------ END ADAPTER


class FakeAgent:
    """A tiny keyword-routing agent so --demo runs offline."""
    RULES = [(("human", "person", "representative", "front desk", "someone"), "transfer"),
             (("book", "appointment", "schedule"), "booking")]

    def __init__(self):
        self.n = 0

    def start(self, caller):
        self.n += 1
        return self.n

    def say(self, session, text):
        t = text.lower()
        for words, step in self.RULES:
            if any(w in t for w in words):
                return step, "Sure, one moment."
        return "greeting", "Hi, how can I help?"


def health_ok():
    """A plain greeting must not land on the fallback step with an empty reply.
    If it does, the agent's model is almost certainly down and every gate would fail falsely."""
    if not FALLBACK_STEP:
        return True
    sid = start_call(DEFAULT_CALLER)
    step, reply = say(sid, "Hello?")
    end_call(sid)
    if step == FALLBACK_STEP and not reply:
        print("\n*** HEALTH CHECK FAILED ***")
        print(f"A greeting landed on the fallback step ({FALLBACK_STEP}) with no reply.")
        print("The agent's language model is probably down (out of credit or rate limited).")
        print("Gate results would be false. Fix the model account and run again. Stopping.\n")
        return False
    print(f"HEALTH OK: greeting -> {step} (the model is answering)\n")
    return True


def run_gate(g):
    name = g["name"]
    caller = g.get("caller", DEFAULT_CALLER)
    setup = g.get("setup", [])
    seen, rows, streak = set(), [], 0
    print(f"===== GATE {name}  (caller={caller}, setup={setup}) =====")
    for line, expected in g["variants"]:
        if line in seen:
            print(f"  [WARN] duplicate line skipped (lines must be distinct): {line!r}")
            continue
        seen.add(line)
        sid = start_call(caller)
        for s in setup:
            say(sid, s)
        step, reply = say(sid, line)
        end_call(sid)
        ok = step == str(expected)
        streak = streak + 1 if ok else 0
        rows.append({"line": line, "expected": str(expected), "observed": step,
                     "reply": reply, "pass": ok, "streak": streak})
        print(f"  [{'PASS' if ok else 'FAIL'}] streak={streak}/5  {line[:46]!r:48} expect {expected} got {step}")
    distinct = len(seen)
    verdict = "GREEN 5/5" if (streak >= 5 and distinct >= 5) else f"NOT GREEN (streak {streak}/5, distinct {distinct})"
    print(f"  --> {name}: {verdict}\n")
    return {"gate": name, "verdict": verdict, "distinct_lines": distinct, "rows": rows}


DEMO = [
    {"name": "greeting_stays", "setup": [],
     "variants": [["Hello?", "greeting"], ["Hi there.", "greeting"], ["Hey there.", "greeting"],
                  ["Hello.", "greeting"], ["Hey.", "greeting"]]},
    {"name": "route_to_booking", "setup": [],
     "variants": [["Uh, can I book an appointment?", "booking"], ["I'm calling to book an appointment.", "booking"],
                  ["Can I come in tomorrow at 10?", "booking"], ["I'd like to schedule a visit, please.", "booking"],
                  ["I need to make an appointment.", "booking"]]},
    {"name": "route_to_transfer", "setup": [],
     "variants": [["I want to speak to a human", "transfer"], ["Can you transfer me to a representative", "transfer"],
                  ["Get me the front desk please", "transfer"], ["I need to talk to a real person", "transfer"],
                  ["Connect me with someone in the office", "transfer"]]},
]


def main():
    global start_call, say, end_call
    args = sys.argv[1:]
    demo = not args or args[0] == "--demo"
    if demo:
        fake = FakeAgent()
        start_call, say, end_call = fake.start, fake.say, (lambda s: None)
        print("DEMO: offline fake agent. One gate is meant to fail, to show what NOT GREEN looks like.\n")
        gates = DEMO
    else:
        if not URL:
            sys.exit("Set VOICE_AGENT_URL, or fill in the ADAPTER section of gate.py.")
        with open(args[0]) as f:
            gates = json.load(f)
    if not health_ok():
        sys.exit(2)
    out_dir = os.path.join(os.path.dirname(os.path.abspath(args[0])) if not demo else ".", "gate_results")
    os.makedirs(out_dir, exist_ok=True)
    results = []
    for g in gates:
        r = run_gate(g)
        results.append(r)
        with open(os.path.join(out_dir, f"gate_results_{g['name']}.json"), "w") as f:
            json.dump(r, f, indent=2)
    print("===== SUMMARY =====")
    for r in results:
        print(f"  {r['gate']:24} {r['verdict']}")
    print(f"\nResults saved to {out_dir}/")


if __name__ == "__main__":
    main()
