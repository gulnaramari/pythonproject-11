import pytest
import re
from collections import Counter
from src.search_on_string import count_, search_on_string


def test_search_string(list_: list[dict[str, [str, int]]]):
    pattern = re.compile(r"\bC\D{6}D\b")
    assert search_on_string(list_, pattern) == [
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        }
    ]


def test_search_string_2(list_wrong: list[dict[str, [str, int]]]):
    pattern = re.compile(r"\bE\D{6}D\b")
    assert search_on_string(list_wrong, pattern) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.5123"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.42557245"},
    ]


def test_count(list_: list[dict[str, [str, int]]]):
    assert count_(list_, ["Перевод организации"]) == Counter({"Перевод организации": 2})


def test_count_2(list_: list[dict[str, [str, int]]]):
    assert count_(list_, ["Перевод организации", "Перевод со счета на счет"]) == Counter(
        ({"Перевод организации": 2, "Перевод со счета на счет": 1})
    )


def test_count_no_status(list_: list[dict[str, [str, int]]]):
    assert count_(list_, []) == Counter()
