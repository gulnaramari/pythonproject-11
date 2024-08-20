import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")

def get_rubl_transactions(transaction:dict) -> float:
	"""Функция принимает одну транзакцию и возвращает ее сумму"""
	amount = float(transaction["operationAmount"]["amount"])
	currency = (transaction["operationAmount"]["currency"]["code"])
	if currency == "RUB":
		return amount
	else:
		API_KEY = os.getenv("API_KEY")
		url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from{from}&amount={amount}"
		headers = {"apikey":API_KEY}
		response = requests.get(url, headers=headers)
		status_code = response.status_code
		if status_code!=200:
			print(f"Неуспешный запрос")
		else:
			result = response.json()
			return result


	if __name__=="__main__":
		transactions = {
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


	get_rubl_transactions(transaction)
	print(get_rubl_transactions)

