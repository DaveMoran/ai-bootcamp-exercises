import time
import functools

from main import ast_timing


@functools.cache
@ast_timing()
def fibonacci_cached(n):
    if n < 2:
        return n
    return fibonacci_cached(n - 2) + fibonacci_cached(n - 1)


@ast_timing()
def snooze(seconds):
    time.sleep(seconds)


@ast_timing()
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


def test_prints_timing_output(capsys):
    """Decorator should print timing information to stdout."""

    factorial(3)
    captured = capsys.readouterr()
    assert "factorial" in captured.out
    assert "->" in captured.out
