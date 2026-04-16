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
