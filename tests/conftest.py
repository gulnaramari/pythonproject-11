from typing import Any
import pandas as pd
import pytest


@pytest.fixture
def test_df() -> pd.DataFrame:
    """Тестовый DataFrame для чтения данных о транзакциях csv или excel"""
    test_dict = {
        "id": [650703.0, 3598919.0],
        "state": ["EXECUTED", "EXECUTED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
        "amount": [16210.0, 29740.0],
        "currency_name": ["Sol", "Peso"],
        "currency_code": ["PEN", "COP"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
        "description": ["Перевод организации", "Перевод с карты на карту"]
    }
    return pd.DataFrame(test_dict)


@pytest.fixture
def test_wrong_df() -> pd.DataFrame:
    """Тестовый DataFrame для чтения неправльных данных о транзакциях csv или excel"""
    test_wrong_dict = {
        "id": [650703.0, 3598919.0],
        "state": ["EXECUTED", "EXECUTED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06S24:00:58Z"],
        "amount": [22210.0, 29740.0],
        "currency_name": ["Sol", "Peso"],
        "currency_code": ["PEN", "COP"],
        "from": ["Счет 58803664561298323391", "Discover 3002601889670065"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
        "description": ["Перевод организации", "Перевод с карты на карту"]
    }
    return pd.DataFrame(test_wrong_dict)

@pytest.fixture
def test_initial_list() -> list[dict[str, Any]]:
    return [{"id": 41428829, "state": "EXECUTED",
             "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "CANCELED",
             "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED",
             "date": "2018-09-12T21:27:25.241689"},
            {"id": 939719570, "state": "EXECUTED",
             "date": "2018-06-30T02:08:58.425572"},
            {"id": 616064591, "state": "FAILED",
             "date": "2022-02-24T08:21:33.419441"},
            {"id": 628064591, "state": "FAILED",
             "date": "2022-02-24T08:21:33.419441"},
            ]


@pytest.fixture
def transactions() -> list[dict[str, Any]]:
    return [{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Translated from organization",
            "from": "Account 75106830613657916952",
            "to": "Account 11776614605963066702"
            },
            {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Transfer from account to account",
            "from": "Account 19708645243227258542",
            "to": "Account 75651667383060284188"
            },
            {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Transfer from account to account",
            "from": "Account 44812258784861134719",
            "to": "Account 74489636417521191160"
            },
            {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Transfer from one card to another",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
            },
            {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Translated from organization",
            "from": "Visa Platinum 1246377376343588",
            "to": "Account 14211924144426031657"
            }]


@pytest.fixture
def start():
    initial_state = {'counter': 0, 'status': 'initialized'}
    yield initial_state
    initial_state['status'] = 'finished'
    print("Final state:", initial_state)


@pytest.fixture
def stop(start):
    # start
    yield
    start['status'] = 'stopped'
    print("Stopped state:", start)
