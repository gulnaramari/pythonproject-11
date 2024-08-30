import re

from typing import Any


def search_on_string(
        transactions: list[dict[str, Any]], string_for_search: re.Pattern
) -> list[dict[str, Any]]:
    """Реализована функция для поиска
    в списке словарей операций по заданной строке
    с использованием re."""
    filtered_transactions = []
    for operation in transactions:
        for value in operation.values():
            match = re.search(string_for_search, str(value))
            if match:
                filtered_transactions.append(operation)
    if filtered_transactions == []:
        print("Data not found")
        return []
    else:
        return filtered_transactions


def count_(transactions: list[dict[str, [str, int]]], list_: list[str]) -> dict[str, int]:
    """функция для подсчета количества банковских операций определенного типа."""
    description_ = []
    for transaction in transactions:
        if transaction.get("description") in list_:
            description_.append(transaction["description"])
    return Counter(description_)


def filter_by_description(transactions: list[dict[str, [str, int]]]) -> list[dict[str, [str, int]]]:
    """Функция для фильтрации транзакций по описанию"""
    user_filter = input('Введите ключевое слово для фильтрации транзакций: ').capitalize()
    filtered_operations = []
    for transaction in transactions:
        if transaction.get("description") == user_filter:
            filtered_operations.append(transaction)

    return filtered_operations