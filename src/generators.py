from typing import Any, Generator

transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Translated from organization",
            "from": "Account 75106830613657916952",
            "to": "Account 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Transfer from account to account",
            "from": "Account 19708645243227258542",
            "to": "Account 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Transfer from account to account",
            "from": "Account 44812258784861134719",
            "to": "Account 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Transfer from one card to another",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Translated from organization",
            "from": "Visa Platinum 1246377376343588",
            "to": "Account 14211924144426031657"
        }
    ]
)


def filter_by_currency(transactions: list[dict[str, Any]],
                       currency: dict) -> Generator[Any, Any, Any]:
    """Function-generator for filtration on valuta"""
    if not transactions:
        raise ValueError("Empty list!")

    for item, currency_list in enumerate(transactions):
        if currency_list["operationAmount"]["currency"]["name"] == currency:
            yield currency_list
            if item == 3:
                break


def transaction_descriptions(transactions: list) -> Generator[Any, Any, Any]:
    """Function-generator for descriptions"""
    if not transactions:
        raise ValueError("Empty list!")
    for description_oper in transactions:
        yield description_oper.get("description")


def card_number_generator(start: int, stop: int) -> Generator[str, Any, None]:
    """Function-generator for numbers of cards"""

    for x in range(start, stop + 1):
        num_null = "0000000000000000"
        card_number = num_null[: -len(str(x))] + str(x)
        card_final = (card_number[:4] + " " + card_number[4:8] +
                      " " + card_number[8:12] + " " + card_number[12:])
        yield f"{card_final}"


for card in card_number_generator(1, 5):
    print(card)

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))


i = filter_by_currency(transactions, "USD")
print(next(i))
print(next(i))
print(next(i))
