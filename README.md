# AI System Optimization Assignment

## Overview

This repository contains my solutions for the AI System Optimization Assignment. The assignment demonstrates practical approaches to AI cost optimization, systematic debugging of multi-agent pipelines, and CI/CD automation using GitHub Actions.

---

## Project Structure

```text
ai-assignment/
│
├── part1-token-optimization/
├── part2-debugging/
└── part3-cicd/
```

---

## Part 1 – Token Optimization

### Problem

The original agent pipeline sends the complete user query and context to every agent, resulting in high token usage, increased latency, and higher inference cost.

### Optimizations Implemented

- Context Compression
- Selective Retrieval
- Skip Reviewer for High-Confidence Responses

### Token Comparison

| Metric | Before | After |
|---------|--------|-------|
| Tokens Used | 4560 | 170 |
| Token Reduction | - | **96.27%** |

### Quality Trade-off

- Context was compressed while preserving relevant information.
- Only necessary documents were retrieved.
- Reviewer execution was skipped only for high-confidence responses.
- Output quality remained nearly unchanged while significantly reducing cost.

---

## Part 2 – Debugging

### Simulated Failures

- Timeout
- Malformed JSON output
- Incorrect response despite successful execution

### Debugging Process

1. Reproduce the issue.
2. Inspect logs and error messages.
3. Identify the failing pipeline component.
4. Validate JSON responses.
5. Check timeout and retry logic.
6. Fix the root cause.
7. Re-test the complete pipeline.

---

## Part 3 – CI/CD

### GitHub Actions Pipeline

The workflow automatically performs:

- Install project dependencies
- Run Flake8 lint checks
- Execute Pytest unit tests
- Deploy to a staging environment after merging into the **main** branch

### Secrets Management

Sensitive information such as API keys, deployment tokens, and credentials should be stored securely using **GitHub Secrets** instead of hardcoding them in the repository.

### Rollback Strategy

If a deployment fails:

1. Stop further deployments.
2. Roll back to the last stable release.
3. Review deployment logs.
4. Identify and fix the root cause.
5. Re-run tests.
6. Deploy the corrected version.

---

## Running the Project

### Part 1

```bash
cd part1-token-optimization

python before.py
python optimized.py
```

### Part 2

```bash
cd part2-debugging

python broken_pipeline.py
```

### Part 3

```bash
cd part3-cicd

python -m pip install -r requirements.txt

python app.py

python -m pytest
```

---

## Technologies Used

- Python
- Flask
- GitHub Actions
- Pytest
- Flake8
- Git
- Visual Studio Code

---

## Assignment Highlights

- Implemented token optimization with measurable cost reduction.
- Simulated and debugged common AI pipeline failures.
- Automated linting and testing using GitHub Actions.
- Demonstrated secure secret management practices.
- Designed a deployment rollback strategy.
- Created a clean, modular project structure.

---

## Author

**Akshitha Mandala**

B.Tech – Electronics and Communication Engineering

---

## License

This project was created as part of an AI System Optimization Internship Assessment.
