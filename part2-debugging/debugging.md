# Part 2 - Debugging Process

## Scenario

The AI pipeline occasionally behaves unexpectedly:

- Sometimes it times out.
- Sometimes it returns malformed JSON.
- Sometimes it returns an incorrect answer even though the pipeline reports success.

---

## Step 1 - Reproduce the Problem

Instead of testing once, I repeatedly execute the pipeline.

Example:

```bash
python broken_pipeline.py
python broken_pipeline.py
python broken_pipeline.py
```

Running multiple times helps reproduce intermittent failures.

---

## Step 2 - Check Logs

I first check which agent fails.

Typical log:

Planner: Creating execution plan...

Retriever: Fetching documents...

Summarizer: Generating response...

Reviewer: Checking response...

This immediately tells me where execution stopped.

---

## Step 3 - Identify Timeout

If execution stops after

Retriever: Fetching documents...

and throws

TimeoutError

I know the retriever service is the source of failure.

Possible reasons:

- Slow API
- Network issue
- Database latency

---

## Step 4 - Validate JSON

The summarizer returns JSON.

Instead of assuming it is valid, I validate it using

```python
json.loads(response)
```

If parsing fails,

I know the LLM generated malformed output.

---

## Step 5 - Check Output Correctness

Sometimes the pipeline finishes successfully but produces incorrect information.

Example

Status: success

Answer: RAG is a database.

The reviewer accepted incorrect information.

This indicates a logic problem rather than a system failure.

---

## Step 6 - Fixes

Timeout

- Add retry logic
- Cache previous results
- Increase timeout limit

Malformed JSON

- Validate JSON
- Retry generation
- Use structured output

Incorrect Answer

- Improve prompts
- Validate retrieved documents
- Add confidence scoring

---

## Tools

During debugging I would use

- Application logs
- Stack traces
- VS Code debugger
- Git history
- Unit tests

---

## Root Cause Isolation

Issue

↓

Find failing agent

↓

Inspect logs

↓

Reproduce consistently

↓

Fix

↓

Regression test

---

## Conclusion

The debugging approach focuses on reproducing failures, identifying the exact component causing the issue, fixing the root cause, and verifying the solution with repeated testing.