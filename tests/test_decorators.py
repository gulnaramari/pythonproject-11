import pytest
from src.decorators import log_decorator, my_function

def test_log_decorator():
    with pytest.raises(Exception, match="NameError"):
        my_function(1, "3")


def test_log_decorator_wrong(capsys):
    captured = capsys.readouterr()
    log_decorator()
    assert captured.out == f"{my_function.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}.\n"