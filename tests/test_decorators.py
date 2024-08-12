import pytest

from src.decorators import log_decorator


def test_log_decorator_1():
    @log_decorator(filename="mylog.txt")
    def function(x, y):
        return x + y

    result = function(1, 0)
    assert result == 1


def test_log_decorator_1_console():
    @log_decorator()
    def function(x, y):
        return x/y

    with pytest.raises(ZeroDivisionError):
        function(1, 0)


def test_log_decorator_no_console(capsys):
    log_decorator(filename="mylog.txt")
    captured = capsys.readouterr()
    assert captured.out == ""


def test_log_decorator_with_console(capsys):
    @log_decorator()
    def test_correct(x, y):
        return x + y

    test_correct(4, 2)
    captured = capsys.readouterr()

    assert captured.out == f"test_correct ok\n"


def test_log_decorator_with_console_error(capsys):
    @log_decorator()
    def test_error(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        test_error(1, 0)
    captured = capsys.readouterr()

    assert captured.out == ("test_error: ZeroDivisionError."
                            " Inputs: (1, 0), {}\n")
