import re

from config import PATH_TO_CSV, PATH_TO_JSON, PATH_TO_XLSX
from src.date_format import date_formatting
from src.processing import filter_by_state, sort_by_date
from src.import_file import transactions_from_csvExcel
from src.search_on_string import filter_by_description, search_on_string
from src.utils import get_data_about_transactions
from src.widget import mask_account_card


def main_menu():

    while True:
        choose_a_method = input("Выберите подходящий метод:"
                                "1 - Получить данные о транзакциях из JSON-файла"
                                "2 - Получить данные о транзакциях из CSV-файла"
                                "3 - Получить данные о транзакциях из XLSX-файла")
        if choose_a_method == "1":
            transactions = get_data_about_transactions(PATH_TO_JSON)
            break
        elif choose_a_method == "2":
            transactions = transactions_from_csvExcel(PATH_TO_CSV)
            break
        elif choose_a_method == "3":
            transactions = transactions_from_csvExcel(PATH_TO_XLSX)
            break
        else:
            continue

    status_for_transactions = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status_ = input("подходящий статус транзакции: EXECUTED, CANCELED, PENDING\n ")
        if status_.upper() in status_for_transactions:
            filtered_transactions = filter_by_state(transactions, status_)
            break
    while True:
        print("\nОтсортировать операции по дате? Да/Нет")
        sorting_by_date = input()
        if sorting_by_date == "нет":
            sorted_transactions = filtered_transactions
            break
        else:
            print("\nОтсортировать по возрастанию или по убыванию?")
            sorting_up_down = input()
            if sorting_by_date.lower() == "да" and sorting_up_down.lower() == "по возрастанию":
                sorted_transactions = sort_by_date(filtered_transactions, is_sort=False)
                break
            elif sorting_by_date.lower() == "да" and sorting_up_down.lower() == "по убыванию":
                sorted_transactions = sort_by_date(filtered_transactions)
                break
            else:
                continue
    while True:
        print("\nВыводить рублевые тразакции? Да/Нет")
        answer = input()
        pattern = re.compile(r"\bRUB\b")
        if answer.lower() == "да":
            new_transactions = search_on_string(sorted_transactions, pattern)
            break
        elif answer.lower() == "нет":
            new_transactions = sorted_transactions
            break
        else:
            continue

    while True:
        print("""\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет""")
        filtered_or_no = input()
        if filtered_or_no.lower() == "да":
            print(
                """\n
Доступные для фильтровки описания: Открытие вклада, Перевод организации, Перевод с карты на карту,
Перевод со счета на счет"""
            )
            total_transaction_list = filter_by_description(new_transactions)
            break
        else:
            total_transaction_list = new_transactions
            break
    print(
        f"\nРаспечатываю итоговый список транзакций...\n\n"
        f"Всего банковских операций в выборке: {len(total_transaction_list)}\n"
    )
    if len(total_transaction_list) == 0:
        print("\nДанных нет")
    else:
        for operation in total_transaction_list:
            date = date_formatting(operation.get("date"))
            if choose_a_method == "1":
                currency_name = operation["operationAmount"]["currency"]["name"]
                amount = operation["operationAmount"]["amount"]
                if operation.get("description") == "Открытие вклада":
                    result = (
                        f"{date} {operation['description']}\n{mask_account_card(operation.get('to'))}\n"
                        f"Сумма: {amount} {currency_name}"
                    )
                else:
                    result = (
                        f"{date} {operation['description']}\n"
                        f"{mask_account_card(operation.get('from'))} -> {mask_account_card(operation.get('to'))}"
                        f"\nСумма: {amount} {currency_name}"
                    )
            else:
                currency_name = operation["currency_name"]
                amount = operation["amount"]
                if operation.get("description") == "Открытие вклада":
                    result = (
                        f"{date} {operation['description']}\n{mask_account_card(operation.get('to'))}\n"
                        f"Сумма: {amount} {currency_name}"
                    )
                else:
                    result = (
                        f"{date} {operation['description']}\n{mask_account_card(operation.get('from'))} -> "
                        f"{mask_account_card(operation.get('to'))}\nСумма: {amount} {currency_name}"
                    )
            print(result)
            print("\n")


if __name__ == "__main__":
    main_menu()
