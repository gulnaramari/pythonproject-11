import json


def get_data_about_transactions(path_to_file: str) -> list:
    """Функция принимает путь до файла, а на выход дает
    список словарей с транзакциями"""
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            try:
                json_data_transactions = json.load(file)
                if json_data_transactions == []:
                    return []
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
    return json_data_transactions


def get_rub_transactions(transaction: dict) -> float:
    """Функция принимает одну транзакцию и возвращает ее сумму в рублях"""
    amount = float(transaction["operationAmount"]["amount"])
    currency = (transaction["operationAmount"]["currency"]["code"])
    if currency == "RUB":
        return float(amount)
    elif currency in ["USD", "EUR"]:
        return "Необходимо конвертировать сумму в рубли"


if __name__ == "__main__":
    path_to_file = "..\\data\\operations.json"
    print(get_data_about_transactions(path_to_file="..\\data\\"
                                      "operations.json"))
