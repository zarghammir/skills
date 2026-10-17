---
name: five-distinct-test
description: For voice AI testing. A readiness gate for each step of a voice agent's call flow - 5 DISTINCT real caller lines per step, ALL must land on the correct next step, and ANY failure resets the streak to 0. Use when someone wants to know whether a call-flow step is "ready", wants a step tested 5 times, or has just edited the flow and needs to check the routing.
---

# five-distinct-test, a readiness gate for voice AI call flows

A voice agent's call flow is a set of steps (greeting, booking, transfer to a person, and so on). After each caller turn, the agent moves to a next step. This skill tests whether each step **routes** correctly:

**5 distinct, real caller lines per step. All 5 must land on the expected next step. Any failure resets the streak to 0.**

One lucky pass proves nothing. Five different phrasings that all route correctly is a step you can trust. The test is read-only: it starts calls, sends caller lines and ends calls. It never edits the flow.

## Before you run it

- Your voice agent needs a text test endpoint: a way to start a conversation, send a caller line, and read back which step the agent is now on. Most voice AI platforms have a playground or test API for this.
- Open `gate.py` and fill in the three small functions in the **ADAPTER** section (`start_call`, `say`, `end_call`) for your platform. The default version talks to a simple JSON API described there. Configure it with the environment variables `VOICE_AGENT_URL` and, if needed, `VOICE_AGENT_TOKEN`.
- **Health guard.** If the agent's language model is down (out of credit, rate limited), many platforms fall back to one step, often "transfer to a person", with an empty reply. Every gate would then fail for the wrong reason. Set `FALLBACK_STEP` to that step's id and the script checks first: if a plain greeting lands there with no reply, it stops and tells you instead of reporting false failures.

## How to run

1. Write a gates file (JSON), one object per step you are testing. Use real caller lines, ideally taken from your own call recordings or transcripts, not lines you made up.
   ```json
   [
     { "name": "greeting_stays", "caller": "+15550000001", "setup": [],
       "variants": [["Hello?", "greeting"], ["Hi there.", "greeting"], ["Hey there.", "greeting"],
                    ["Hello.", "greeting"], ["Hey.", "greeting"]] },
     { "name": "new_or_returning", "caller": "+15550000001", "setup": ["I want to book an appointment"],
       "variants": [["I'm a new customer, first visit", "new_customer"], ["This is my first time", "new_customer"],
                    ["New appointment please, never been before", "new_customer"],
                    ["I've been there before", "returning_customer"], ["I'm an existing customer", "returning_customer"]] }
   ]
   ```
   - `caller`: the caller's number, if your agent behaves differently for known and unknown callers. Use made-up test numbers.
   - `setup`: caller lines sent first, to walk the call to the step under test.
   - `variants`: `[caller line, expected next step]`, at least 5 distinct lines.
2. Run:
   ```bash
   python3 gate.py /path/to/gates.json
   python3 gate.py --demo     # offline demo against a tiny built-in fake agent
   ```
3. Read the PASS/FAIL and streak for each line, the verdict for each gate (**GREEN 5/5** or **NOT GREEN**), and the saved `gate_results/gate_results_<name>.json`.

## Reading the results

- **GREEN 5/5**: the step is ready. 5 distinct lines, all correct, streak reached 5.
- **NOT GREEN**: a line landed on the wrong step. Decide which kind of failure it is:
  - **Content failure.** The routing was wrong but allowed: the step's condition is too loose or too tight. Change that step's condition in your flow, **reset the streak**, and run the gate again.
  - **Engine failure.** A jump the flow cannot express, or the model is down. Stop and report it. Don't paper over it by rewording prompts.
- Change only the flow's step definitions. Don't change the platform's code to make a gate pass.

## Notes

- Steps that wait on a real outside system (booking a slot, writing a customer record) can usually only be tested for **routing into the step** in a playground. Completing them needs the real integration.
- Duplicate lines in a gate are skipped with a warning, and the gate cannot go green without 5 distinct lines.
