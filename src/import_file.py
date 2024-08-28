import csv

import pandas as pd


def transaction_from_csv(file: str) -> list[dict]:
    """Function gets data from csv file and gives list of dictionaries"""
    transaction_ = []
    try:
        with open(file, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            header = next(reader)
            for row in reader:
                row_dict = {
                    "id": row[header.index("id")],
                    "state": row[header.index("state")],
                    "date": row[header.index("date")],
                    "operationAmount": {
                        "amount": row[header.index("amount")],
                        "currency": {
                            "name": row[header.index("currency_name")],
                            "code": row[header.index("currency_code")],
                        },
                    },
                    "description": row[header.index("description")],
                    "from": row[header.index("from")],
                    "to": row[header.index("to")],
                }
                transaction_.append(row_dict)
    except Exception:
        return []
    return transaction_


def transaction_from_excel(file: str) -> list[dict]:
    """Функция считывающая файл в формате excel и возвращающая список словарей"""
    df = pd.read_excel(file)
    result_ = []
    count_ = len(df)
    for i in range(0, count_):
        dict_r = {
            "id": df.at[i, "id"],
            "state": df.at[i, "state"],
            "date": df.at[i, "date"],
            "operationAmount": {
                "amount": df.at[i, "amount"],
                "currency": {
                    "name": df.at[i, "currency_name"],
                    "code": df.at[i, "currency_code"],
                },
            },
            "description": df.at[i, "description"],
            "from": df.at[i, "from"],
            "to": df.at[i, "to"],
        }
        result_.append(dict_r)
    return result_


if __name__ == "__main__":
    result = transaction_from_excel("..\\data\\transactions_excel.xlsx")
    print(result)


if __name__ == "__main__":
    result = transaction_from_csv("..\\data\\transactions.csv")
    print(result)