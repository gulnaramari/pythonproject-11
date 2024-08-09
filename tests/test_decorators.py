import pytest
from src.decorators import log_decorator, function


def test_log_decorator(capsys):
    log_decorator(filename="mylog.txt")
    captured = capsys.readouterr()
    assert captured.out == (f"{my_function.__name__} error: {e.__class__.__name__}."
                            f" Inputs: {args}, {kwargs}.\n")
