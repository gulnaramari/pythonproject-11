from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_data: str) -> str:
    """Функция маскировки карты или счета"""
    for arg in input_data:
        if not isinstance(arg, str):
            raise TypeError("Ошибка типа данных")

    if "Account" in input_data:
        return get_mask_account(input_data)
    else:
        return get_mask_card_number(input_data)


print(mask_account_card("Account 73654108430135874305"))


def get_date(input_data: str) -> str:
    """Функция преобразования даты"""
    for arg in input_data:
        if not isinstance(arg, str):
            raise TypeError("Ошибка типа данных")
    if len(input_data) == 26 and input_data[10] == "T":
        date = input_data.split("T")[0]
        slice_date = f"{date[-2:]}.{date[5:7]}.{date[:4]}"
    else:
        raise ValueError("Некорректно введены данные")
    return slice_date


print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Account 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))
