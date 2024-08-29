import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/utils.log",
    filemode="w",
)

logger = logging.getLogger("utils")


def get_data_about_transactions(path_to_file: str) -> list:
    """Функция принимает путь до файла, а на выход дает
    список словарей с транзакциями"""
    try:
        logger.info("Request for file path")
        with open(path_to_file, "r", encoding="utf-8") as file:
            try:
                logger.info("The list of dictionaries has been created")
                json_data_transactions = json.load(file)
                if json_data_transactions == []:
                    logger.info("No dictionaries has been created")
                    return []
            except json.JSONDecodeError:
                logger.error("Decode error")
                return []
    except FileNotFoundError:
        logger.error("File was not found")
        return []
    return json_data_transactions


def get_rub_transactions(transaction: dict) -> float:
    """Функция принимает одну транзакцию и возвращает ее сумму в рублях"""
    logger.info("Getting the transaction data")
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        logger.info(f"Operation amount in RUB:{amount}")
        return float(amount)
    elif currency in ["USD", "EUR"]:
        logger.error("Operation amount can't be done")
        print("Operation amount can't be done")


if __name__ == "__main__":
    path_to_file = "..\\data\\operations.json"
    print(get_data_about_transactions(path_to_file="..\\data\\" "operations.json"))
