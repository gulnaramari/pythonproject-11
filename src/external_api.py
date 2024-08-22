import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")
api_key = os.getenv("API_KEY")

load_dotenv()

# Проверка загрузки API_KEY
api_key = os.getenv("API_KEY")
print(f" ")


def get_rub_transactions(transaction: dict) -> float:
    """Функция принимает одну транзакцию и возвращает ее сумму"""
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return float(amount)
    elif currency in ["USD", "EUR"]:
        url = (f"https://api.apilayer.com/exchangerates_data/convert?"
               f"to=RUB&from={currency}&amount={amount}")
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        json_result = response.json()
        amount_rub = json_result["result"]
        return amount_rub
    else:
        return None


if __name__ == "__main__":
    transaction = {
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
r = get_rub_transactions(transaction={
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
        })
print(r)


if __name__ == "__main__":
    transaction = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }
    r = get_rub_transactions(transaction={
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    })
print(r)

