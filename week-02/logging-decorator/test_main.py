from main import ast_log
import logging


@ast_log(logging.DEBUG)
def add(a, b):
    return a + b


def test_ast_log_defaults(caplog):

    with caplog.at_level(logging.DEBUG):
        add(3, 5)

    assert "DEBUG" in caplog.text
    assert "add" in caplog.text


@ast_log(logging.DEBUG, name="Subtraction")
def sub(a, b):
    return a - b


def test_with_custom_name(caplog):

    with caplog.at_level(logging.DEBUG):
        sub(3, 5)

    assert "DEBUG" in caplog.text
    assert "Subtraction" in caplog.text


@ast_log(logging.DEBUG, message="Custom Message")
def mult(a, b):
    return a * b


def test_with_custom_msg(caplog):

    with caplog.at_level(logging.DEBUG):
        mult(3, 5)

    assert "DEBUG" in caplog.text
    assert "Custom Message" in caplog.text
