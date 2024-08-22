import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/mask.log",
    filemode="w",
)

logger = logging.getLogger("mask")


def get_mask_card_number(input_data: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску"""
    for arg in input_data:
        if not isinstance(arg, str):
            raise TypeError("Ошибка типа данных")

    new_cardnumber = ""
    new_cardname = ""
    if "Account" in input_data:
        raise ValueError("Некорректное название карты")
    else:
        for symbol in input_data:
            if symbol.isdigit():
                new_cardnumber += symbol
            elif symbol.isalpha():
                new_cardname += symbol
    if len(new_cardnumber) == 16:
        if new_cardnumber[0] != "0":
            slice_1 = new_cardnumber[0:4]
            slice_2 = new_cardnumber[4:6]
            slice_3 = new_cardnumber[-4:]
            mask_card = slice_1 + " " + slice_2 + "** **** " + slice_3
        else:
            raise ValueError("Некорректный номер карты")
    else:
        raise ValueError("Некорректный номер карты")
    return (f"{new_cardname} {mask_card}")


def get_mask_account(input_data: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску"""
    new_accountname = ""
    for arg in input_data:
        if not isinstance(arg, str):
            raise TypeError("Ошибка типа данных")
    new_number = ""
    new_name = ""
    if "Account" in input_data:
        for symbol in input_data:
            if symbol.isalpha():
                new_accountname += symbol
                new_name += symbol
            elif symbol.isdigit():
                new_number += symbol
        slice_number = new_number[-4:]
        mask_account = "**" + slice_number
        return (f"{new_accountname} {mask_account}")
    else:
        raise ValueError("Некорректный ввод")

    if len(new_number) == 20:
        if new_number[0] != "0":
            slice_number = new_number[-4:]
            mask_account = "**" + slice_number
    else:
        raise ValueError("Некорректный номер счета")
    return (f"{new_name} {mask_account}")
