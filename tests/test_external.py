import os
from unittest.mock import patch

import pytest
from dotenv import load_dotenv

from src.external_api import get_rub_transactions

load_dotenv(".env")
api_key = os.getenv("api_key")


@pytest.fixture
def transaction_in_rub():
    return "RUB", 48223.05


@pytest.fixture
def transaction_in_usd():
    return 48223.05


transaction = {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    }
}


def test_get_rub_transactions_from_rub(transaction_in_rub):
    assert get_rub_transactions(transaction) == 48223.05


transaction_usd_correct = {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "2.0",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        }
}


def test_get_rub_transactions_correct_from_usd(transaction_in_usd):
    assert get_rub_transactions(transaction_usd_correct) == 183.35


@pytest.fixture
def transaction_in_usd_wrong():
    return 482.45


transaction_wrong = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": 2.0,
        "currency": {
          "name": "USD",
          "code": ""
        }
    }
}


def test_get_rub_transactions_wrong(transaction_in_usd_wrong):
    assert get_rub_transactions(transaction_wrong) == None


@patch("requests.request")
def test_get_rub_transactions_correct_from_usd_1(mock_get):
    mock_get.return_value.json.return_value = {"result": 183.35}
    assert get_rub_transactions(transaction_usd_correct) == 183.35
    mock_get.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/"
        "convert?to=RUB&from=USD&amount=2.0",
        headers={"api_key": "GWXUgoP8ncjVagpxkWwJzrzksblrMRo8"},
        )
