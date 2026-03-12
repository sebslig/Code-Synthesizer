# OpenClaw Code Synthesizer

An autonomous agent system built on the OpenClaw framework that converts natural language requirements into fully tested, PEP 8 compliant Python code.

## Overview

This project implements a multi-agent architecture to automate the software development lifecycle for small-to-medium Python functions. It utilizes:

1.  **Spec Analyst Agent**: Refines vague natural language into technical specifications.
2.  **Architect Agent**: Determines the best implementation strategy and edge cases.
3.  **Coder Agent**: Generates the actual Python implementation.
4.  **QA Tester Agent**: Writes and executes unit tests to verify correctness.

## Key Features

*   **Self-Correction**: Agents communicate to fix bugs found during the testing phase.
*   **OpenClaw Powered**: Leverages the OpenClaw orchestration layer for agent communication.
*   **Security Focused**: Includes basic sanitization for generated code.
*   **Type Hinting**: Ensures all generated code includes modern Python type hints.

## Installation

```bash
git clone https://github.com/username/openclaw-coder.git
cd openclaw-coder
pip install -r requirements.txt
```

## Configuration

Set your API keys in a `.env` file:

```env
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

## Usage

Run the main agent loop:

```python
from src.orchestrator import CodeGenOrchestrator

orchestrator = CodeGenOrchestrator()
result = orchestrator.run("Create a function that calculates the Fibonacci sequence up to N terms.")
print(result['code'])
```

## Structure

*   `src/agents/`: Individual OpenClaw agent definitions.
*   `src/tools/`: Tools for file I/O and code execution.
*   `tests/`: Unit tests for the agent framework itself.

## Architecture

The system follows a sequential chain:
Input -> [Spec Analyst] -> [Coder] -> [Tester] -> Output

If testing fails, the Coder receives the traceback and attempts a fix (up to 3 retries).
