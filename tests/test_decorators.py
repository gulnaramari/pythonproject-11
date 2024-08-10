from datetime import datetime

import pytest

from src.decorators import function, log_decorator


def test_log_decorator_1():
    @log_decorator(filename="mylog.txt")
    def function(x, y):
        return x + y

    result = function(3, 5)
    assert result == 8


def test_log_decorator_in_console():
    @log_decorator()
    def function(x, y):
        return x + y

    result = function(3, 5)
    assert result == 8


def test_log_decorator_2():
    @log_decorator(filename="mylog.txt")
    def function(x, y):
        return x + y

    result = function(-1, 5)
    assert result == 4


def test_log_decorator_wrong_type():
    log_decorator(filename="mylog.txt")
    with pytest.raises(TypeError):
        function(1, "8")


def test_log_decorator_no_console(capsys):
    log_decorator(filename="mylog.txt")
    captured = capsys.readouterr()
    assert captured.out == ''


def test_log_decorator_with_console(capsys):
    # Вызов функции для создания лога
    function(1, 2)
    time_1 = datetime.now()
    time_2 = datetime.now()
    # Чтение захваченного вывода
    captured = capsys.readouterr()
    assert (f"function ok. Begin of work:{time_1}."
            f" Final of work {time_2}.\n") in captured.out
