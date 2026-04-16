import pytest
from mcp.server.fastmcp.exceptions import ToolError
from main import greet, add_numbers, word_stats, safe_divide


def test_greet_casual() -> None:
    result = greet("Alice")
    assert result == "Hey, Alice!"


def test_greet_formal() -> None:
    result = greet("Bob", formal=True)
    assert result == "Good day, Bob."


def test_add_numbers_integers() -> None:
    result = add_numbers(2, 3)
    expected = {"a": 2, "b": 3, "sum": 5, "is_integer": True}
    assert result == expected


def test_add_numbers_floats() -> None:
    result = add_numbers(2.5, 3.7)
    expected = {"a": 2.5, "b": 3.7, "sum": 6.2, "is_integer": False}
    assert result == expected


def test_word_stats() -> None:
    text = "Hello world! Hello everyone. This is a test."
    result = word_stats(text)
    assert result["word_count"] == 8
    assert result["char_count"] == len(text)
    assert result["line_count"] == 1
    assert result["most_common_word"] == "hello"


def test_safe_divide_normal() -> None:
    result = safe_divide(10, 2)
    assert result == 5.0


def test_safe_divide_by_zero() -> None:
    with pytest.raises(ToolError) as exc_info:
        safe_divide(10, 0)
    assert "cannot divide by zero" in str(exc_info.value).lower()
