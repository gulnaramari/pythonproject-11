from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, masks_number",
    [
        (7000892289606361, "7000 89** **** 6361"),
        (70007922896063, "Введите корректный номер карты"),
        (7365410843013587430500, "Введите корректный номер карты"),
        ("", "Введите корректный номер карты"),
    ],
)
def test_get_mask_card_number(card_number: str, masks_number: str) -> Any:
    assert get_mask_card_number(card_number) == masks_number


@pytest.mark.parametrize(
    "account_number, masks_account",
    [
        (7000792289606361, "Введите корректный номер счета"),
        (736541084301358743052, "Введите корректный номер счета"),
        (73654108430135874305, "**4305"),
        ("", "Введите корректный номер счета"),
    ],
)
def test_get_mask_account(account_number: str, masks_account: str) -> Any:
    assert get_mask_account(account_number) == masks_account
