import json

import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")


def get_rub_transactions(transaction: dict) -> float:
	"""Функция принимает одну транзакцию и возвращает ее сумму"""
	amount = float(transaction["operationAmount"]["amount"])
	currency = (transaction["operationAmount"]["currency"]["code"])
	if currency == "RUB":
		return float(amount)
	else:
		API_KEY = os.getenv("API_KEY")
		url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from{from}&amount={amount}"
		headers = {"apikey": API_KEY}
		response = requests.get(url, headers=headers)
		status_code = response.status_code
		if status_code == 200:
			return round(response.json["rates"]["RUB"] * amount, 2)
		else:
			print(f"Неуспешный запрос")



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
r=get_rub_transactions(transaction={
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


def get_rate_exchange(currency: str, API_KEY: str) -> float:
    """Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
	и конвертации суммы операции в рубли"""
    headers = {"apikey": API_KEY}
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        if "RUB" in result["rates"]:
            return result["rates"]["RUB"]
        else:
            raise ValueError("Ошибка данных")
    else:
        print(f"Неуспешный запрос")


if __name__ == "__main__":
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }
    try:
        res = get_rate_exchange("USD", "GWXUgoP8ncjVagpxkWwJzrzksblrMRo8")
        print(res)
    except Exception as e:
        print(f"Error occurred: {e}")
