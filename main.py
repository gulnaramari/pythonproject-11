import re

from config import PATH_TO_CSV, PATH_TO_JSON, PATH_TO_XLSX
from src.date_format import date_formatting
from src.processing import filter_by_state, sort_by_date
from src.import_file import transactions_from_csvExcel
from src.search_on_string import filter_by_description, search_on_string
from src.utils import get_transactions
from src.widget import mask_account_card


def main():

    print(
        """Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n"""
    )
    transactions_state = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        input_ = input("Выберите подходящий пункт: ")
        if input_ == "1":
            print("\nДля обработки выбран JSON-файл.")
            transactions = get_transactions(PATH_TO_JSON)
            break
        elif input_ == "2":
            print("\nДля обработки выбран CSV-файл.")
            transactions = transactions_from_csvExcel(PATH_TO_CSV)
            break
        elif input_ == "3":
            print("\nДля обработки выбран XLSX-файл.")
            transactions = transactions_from_csvExcel(PATH_TO_XLSX)
            break
        else:
            continue

    while True:
        state_input = input("\nВведите статус, по которому необходимо выполнить фильтрацию.\n "
                                  "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n ")
        if state_input.upper() not in transactions_state:
            print(f"\nСтатус операции {state_input} недоступен.")
        else:
            filtered_transactions = filter_by_state(transactions, state_input)
            break
    while True:
        print("\nОтсортировать операции по дате? Да/Нет")
        sorting_by_date = input()
        if sorting_by_date.lower() == "да":
            print("\nОтсортировать по возрастанию или по убыванию?")
            sorting_up_down = input()
            if sorting_by_date.lower() == "да" and sorting_up_down.lower() == "по возрастанию":
                sorted_transactions = sort_by_date(filtered_transactions, reverse=False)
                break
            elif sorting_by_date.lower() == "да" and sorting_up_down.lower() == "по убыванию":
                sorted_transactions = sort_by_date(filtered_transactions)
                break
            else:
                continue
        elif sorting_by_date == "нет":
            sorted_transactions = filtered_transactions
            break
        else:
            continue
    while True:
        print("\nВыводить только рублевые транзакции? Да/Нет")
        answer = input()
        pattern = re.compile(r"\bRUB\b")
        if answer.lower() == "да":
            user_transactions = search_on_string(sorted_transactions, pattern)
            break
        elif answer.lower() == "нет":
            user_transactions = sorted_transactions
            break
        else:
            continue

    while True:
        print("""\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет""")
        word_filter = input()
        if word_filter.lower() == "да":
            print(
                """\n
Доступные для фильтровки описания: Открытие вклада, Перевод организации, Перевод с карты на карту,
Перевод со счета на счет"""
            )
            transaction_list = filter_by_description(user_transactions)
            break
        else:
            transaction_list = user_transactions
            break
    print(
        f"\nРаспечатываю итоговый список транзакций...\n\n"
        f"Всего банковских операций в выборке: {len(transaction_list)}\n"
    )
    if len(transaction_list) == 0:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        for operation in transaction_list:
            date = date_formatting(operation.get("date"))
            if input_ == "1":
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
    main()
