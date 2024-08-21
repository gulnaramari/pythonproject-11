import json
import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")
api_key = os.getenv("API_KEY")


def get_rub_transactions(transaction: dict) -> float:
    """Функция принимает одну транзакцию и возвращает ее сумму"""
    amount = float(transaction["operationAmount"]["amount"])
    currency = (transaction["operationAmount"]["currency"]["code"])
    if currency == "RUB":
        return float(amount)
    elif currency in ["USD","EUR"]:
        url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=2"
        payload = {}
        headers = {"apikey": "GWXUgoP8ncjVagpxkWwJzrzksblrMRo8"}
        response = requests.request("GET", url, headers=headers, data = payload)

        status_code = response.status_code
        print(f"Статус код {status_code}")
        if status_code == 200:
            response_text = json.loads(response.text)
            res = response_text['result']
            return round(res, 1)
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

