# AI System Optimization Assignment

## Overview

This repository contains solutions for three technical tasks:

1. Token / Cost Optimization
2. Debugging an AI Pipeline
3. CI/CD Pipeline

---

## Project Structure

```
ai-assignment/
│
├── part1-token-optimization/
├── part2-debugging/
└── part3-cicd/
```

---

# Part 1 – Token Optimization

### Problem

The original pipeline sends the complete user query to every agent.

Pipeline:

User Query

↓

Planner

↓

Retriever

↓

Summarizer

↓

Reviewer

This results in high token usage and increased latency.

### Optimizations

- Context Compression
- Selective Retrieval
- Skip Reviewer for High-Confidence Responses

### Token Comparison

| Version | Tokens |
|----------|--------|
| Before | 4560 |
| After | 170 |

Reduction:

**96.27%**

---

# Part 2 – Debugging

The broken pipeline simulates three real-world failures.

- Timeout
- Malformed JSON
- Incorrect response despite success status

Debugging Process

- Reproduce issue
- Inspect logs
- Validate JSON
- Isolate failing component
- Fix issue
- Re-test

---

# Part 3 – CI/CD

GitHub Actions workflow performs:

- Install dependencies
- Run Flake8
- Run Unit Tests
- Deploy to staging after merge to main

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

## Technologies

- Python
- Flask
- GitHub Actions
- Pytest
- Flake8

---

## Author

Akshitha Mandala