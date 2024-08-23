import logging

from src.masks import get_mask_account, get_mask_card_number

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/main.log",
    filemode="w",
)

logger = logging.getLogger("main")


def mask_account_card(input_data: str) -> str:
    """Функция маскировки карты или счета"""
    logger.info("Card or account number data received")
    for arg in input_data:
        if not isinstance(arg, str):
            raise TypeError("Data type error")

    if "Account" in input_data:
        return get_mask_account(input_data)
    else:
        return get_mask_card_number(input_data)


print(mask_account_card("Account 73654108430135874305"))
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Account 73654108430135874305"))
