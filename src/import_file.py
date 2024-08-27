import csv

import pandas as pd


def transaction_from_csv(file: str) -> list[dict]:
    """Function gets data from csv file and gives list of dictionaries"""
    transaction_ = []
    try:
        with open(csv_path, encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file, delimiter=";")
            next(reader)
            for row in reader:
                dict_ = {
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
                transaction_.append(dict_)
    except Exception:
        return []
    return transaction_


if __name__ == "__main__":
    result = transaction_from_csv("..\\data\\transactions.csv")
    print(result)


def transaction_from_excel(file: str) -> list[dict]:
    """Функция считывающая файл в формате excel и возвращающая список словарей"""
    df = pd.read_excel(file)
    result = []
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
        result.append(dict_r)
    return result


if __name__ == "__main__":
    result = transaction_from_excel("..\\data\\transactions_excel.xlsx")
    print(result)
