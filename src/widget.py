from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_data: str) -> str:
    """Функция маскирующая номер карты или счёта"""
    for arg in input_data:
        if not isinstance(arg, str):
            raise TypeError("Data type error")
    if "Visa" in input_data and 21 <= len(input_data) <= 30:
        card_number = input_data[-16:]
        mask_card_number = input_data.replace(
            input_data[-16:], get_mask_card_number(card_number)
        )
        return mask_card_number
    elif "Maestro" in input_data and len(input_data) == 24:
        card_number = input_data[-16:]
        mask_card_number = input_data.replace(
            input_data[-16:], get_mask_card_number(card_number)
        )
        return mask_card_number
    elif "Mastercard" in input_data.capitalize() and len(input_data) == 27:
        card_number = input_data[-16:]
        mask_card_number = input_data.replace(
            input_data[-16:], get_mask_card_number(card_number)
        )
        return mask_card_number
    elif "Счет" in input_data and len(input_data) == 25:
        account_number = input_data[-20:]
        mask_account_number = input_data.replace(
            input_data[-20:], get_mask_account(account_number)
        )
        return mask_account_number
    elif "Discover" in input_data and len(input_data) == 25:
        card_number = input_data[-16:]
        mask_card_number = input_data.replace(
            input_data[-16:], get_mask_card_number(card_number)
        )
        return mask_card_number
    elif "American Express" in input_data and len(input_data) == 33:
        card_number = input_data[-16:]
        mask_card_number = input_data.replace(
            input_data[-16:], get_mask_card_number(card_number)
        )
        return mask_card_number
    else:
        return "Неверные данные"


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


print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))

print(get_date("2024-03-11T02:26:18.671407"))
