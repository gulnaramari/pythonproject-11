import pytest
from src.decorators import log_decorator, function


def test_log_decorator():
    @log_decorator(filename="mylog.txt")
    def function(x, y):
        return x + y

    result = function(3, 5)
    assert result == 8


def test_log_decorator_wrong_type():
    with pytest.raises(Exception, match="TypeError"):
        function("4", "7")


def test_log_decorator_error():
    with pytest.raises(Exception, match="ValueError"):
         function()


def test_log_decorator_consol(capsys):
    log_decorator(filename="mylog.txt")
    captured = capsys.readouterr()
    assert captured.out == (f"{function.__name__} error: {e.__class__.__name__}."
                            f" Inputs: {args}, {kwargs}.\n")
