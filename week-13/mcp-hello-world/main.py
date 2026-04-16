from collections import Counter

import string

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
    if formal:
        return f"Good day, {name}."
    return f"Hey, {name}!"


@mcp.tool()
def add_numbers(a: float, b: float) -> dict[str, float | bool]:
    """
    Add two numbers and return the result with metadata.

    Returns a dict with keys: 'a', 'b', 'sum', and 'is_integer'
    (True if the sum has no decimal component).
    """
    # TODO: implement — return a dict, not just the sum
    return {"a": a, "b": b, "sum": a + b, "is_integer": (a + b).is_integer()}


@mcp.tool()
def word_stats(text: str) -> dict[str, int | str]:
    """
    Return basic statistics about a block of text.

    Returns a dict with: 'word_count', 'char_count', 'line_count',
    and 'most_common_word' (the word that appears most often, lowercased,
    ignoring punctuation).
    """
    return {
        "word_count": len(text.split()),
        "char_count": len(text),
        "line_count": len(text.split("\n")),
        "most_common_word": Counter(
            text.translate(str.maketrans("", "", string.punctuation)).lower().split()
        ).most_common(1)[0][0],
    }


@mcp.tool()
def safe_divide(numerator: float, denominator: float) -> float:
    """
    Divide numerator by denominator.

    Raises a ToolError if denominator is zero, with a message that
    explains what happened and what the caller should do instead.
    Returns the quotient as a float.
    """
    if denominator == 0:
        raise ToolError(
            "You cannot divide by zero. Try again with a different denominator"
        )
    return numerator / denominator


if __name__ == "__main__":
    mcp.run(transport="stdio")
