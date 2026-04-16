# Exercise 2: FastMCP Hello World — Your First Tool
**Topic:** FastMCP tool declaration, type hints, ToolError  
**Due:** Friday morning/evening  
**Time Estimate:** 60 minutes  
**Difficulty:** ⭐ Easy

## Description

Before you write your first real file system tool in Week 14, write a few toy tools to get comfortable with FastMCP's decorator pattern, type hint integration, and error handling. This is muscle memory practice — small, fast, deliberately simple.

Create `exercises/week13/ex2_fastmcp_hello.py`. This file is standalone and does not need to be part of the `fs-mcp-server` package — it's a scratch pad.

## Part A — Three tools, three return types

Implement these three tools:

```python
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.exceptions import ToolError

mcp = FastMCP("week13-hello")


@mcp.tool()
def greet(name: str, formal: bool = False) -> str:
    """
    Greet a person by name.

    `name` is the person's name. `formal` controls whether the greeting
    is formal ('Good day, Name.') or casual ('Hey, Name!'). Returns the
    greeting as a string.
    """
    # TODO: implement
    pass


@mcp.tool()
def add_numbers(a: float, b: float) -> dict:
    """
    Add two numbers and return the result with metadata.

    Returns a dict with keys: 'a', 'b', 'sum', and 'is_integer'
    (True if the sum has no decimal component).
    """
    # TODO: implement — return a dict, not just the sum
    pass


@mcp.tool()
def word_stats(text: str) -> dict:
    """
    Return basic statistics about a block of text.

    Returns a dict with: 'word_count', 'char_count', 'line_count',
    and 'most_common_word' (the word that appears most often, lowercased,
    ignoring punctuation).
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    mcp.run(transport="stdio")
```

## Part B — Add intentional error handling

Add a fourth tool that demonstrates `ToolError`:

```python
@mcp.tool()
def safe_divide(numerator: float, denominator: float) -> float:
    """
    Divide numerator by denominator.

    Raises a ToolError if denominator is zero, with a message that
    explains what happened and what the caller should do instead.
    Returns the quotient as a float.
    """
    # TODO: implement — use ToolError for the zero division case,
    # NOT a bare Python exception or ZeroDivisionError
    pass
```

The key distinction to practise: `raise ToolError("...")` sends a structured error back to the model via the protocol. `raise ZeroDivisionError` crashes the handler uncleanly. Use the right one.

## Part C — Connect to Inspector and test all four tools

Run the server and call each tool from Inspector. Verify:
- `greet("Dave", formal=True)` → `"Good day, Dave."`
- `greet("Dave")` → `"Hey, Dave!"`
- `add_numbers(3.5, 1.5)` → `{"a": 3.5, "b": 1.5, "sum": 5.0, "is_integer": true}`
- `word_stats("hello world hello")` → `{"word_count": 3, "char_count": 19, "line_count": 1, "most_common_word": "hello"}`
- `safe_divide(10, 2)` → `5.0`
- `safe_divide(10, 0)` → `isError: true` with your message

## Part D — Write tests

Create `exercises/week13/tests/test_ex2_fastmcp_hello.py`. Write at least one test per tool, including the error case for `safe_divide`. You don't need MCP infrastructure for this — test the underlying functions directly.

## Learning Goals
- Get comfortable with `@mcp.tool()` decorator syntax and type hint integration
- Understand how return types become the tool's response content
- Understand the difference between `ToolError` and unhandled exceptions
- Practice writing the kind of docstring descriptions that work well as model-facing prompts

## Acceptance Criteria
- [x] All four tools implemented and passing Inspector tests
- [x] `safe_divide(10, 0)` returns `isError: true` via `ToolError`, not an unhandled exception
- [x] `word_stats` handles multi-line text and punctuation correctly
- [x] Docstrings follow the quality pattern from the Week 13 breakdown — purpose, parameter semantics, return value, error cases
- [x] `pytest` tests pass for all four tools including the zero-division error case
- [x] `mypy`, `ruff`, `black` all pass cleanly