from unittest.mock import patch

import pytest

from src.utils import get_transactions


def test_get_transactions():
    """тест на пустой список"""
    assert get_transactions("[]") == []


def test_get_data_about_transactions_wrong():
    """тест на неправильный путь"""
    assert get_transactions(path_to_file="..\\main"
                                                    "\\operations.json") == []


@pytest.fixture
def get_correct_path(): return '../data/operations.json'


@pytest.fixture
def get_wrong_path(): return 'nothing'


@pytest.fixture
def get_wrong_file():
    return '../data/wrong_operations.json'


@patch("builtins.open")
def test_get_transactions_1(open_mock):
    open_mock.return_value.__enter__.return_value.read.return_value =\
        ('[{"name": "dict"}, {"name": "user_name"}]')
    assert (get_transactions("path_my") ==
            [{"name": "dict"}, {"name": "user_name"}])
    open_mock.assert_called_once_with("path_my", 'r', encoding='utf-8')


def test_get_data_about_transactions_(get_correct_path):
    assert get_transactions(get_correct_path)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


def test_get_data_about_transactions_wrong_1(get_wrong_path):
    assert get_transactions(get_wrong_path) == []


def test_get_data_about_transactions_none(get_wrong_file):
    assert get_transactions(get_wrong_file) == []
