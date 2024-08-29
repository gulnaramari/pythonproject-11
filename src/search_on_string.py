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
