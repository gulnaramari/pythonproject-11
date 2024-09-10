import json
from unittest.mock import Mock

from config import PATH_TO_JSON
from src.utils import get_transactions


def test_get_transactions():
    mock_json = Mock(
        return_value=[
            {
                "id": 782295999,
                "state": "EXECUTED",
                "date": "2019-09-11T17:30:34.445824",
                "operationAmount": {
                    "amount": "54280.01",
                    "currency": {"name": "USD", "code": "USD"},
                },
                "description": "Перевод организации",
                "from": "Счет 24763316288121894080",
                "to": "Счет 96291777776753236930",
            }
        ]
    )
    json.load = mock_json
    assert get_transactions(PATH_TO_JSON) == [
        {
            "id": 782295999,
            "state": "EXECUTED",
            "date": "2019-09-11T17:30:34.445824",
            "operationAmount": {
                "amount": "54280.01",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 24763316288121894080",
            "to": "Счет 96291777776753236930",
        }
    ]


def test_get_transactions_without_path():
    result = get_transactions("")
    assert result == []
