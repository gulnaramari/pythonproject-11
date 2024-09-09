from typing import Any

import pytest

from src.widget import mask_account_card
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("input_data, expected_mask", [
                        ("Visa Classic 683198247673765",
                         None),
                        ("MasterCard 71583007347267588900",
                         None),
                         ])
def test_get_mask_card_number(input_data: str, expected_mask: str) -> Any:
    assert get_mask_card_number(input_data) == expected_mask


def test_get_invalid_mask_card_number(input_data: str) -> Any:
    with pytest.raises(ValueError):
        get_mask_card_number("12345678")


def test_get_invalid_name_card_number(input_data: str) -> Any:
    with pytest.raises(ValueError):
        get_mask_card_number("12opyu3456kljh78")


def test_short_get_mask_card_number(input_data: str) -> Any:
    with pytest.raises(ValueError):
        get_mask_card_number("1")


def test_get_empty_mask_card_number(input_data: str) -> Any:
    with pytest.raises(ValueError):
        get_mask_card_number("Visa Classic")


def test_get_none_mask_card_number(input_data: str) -> Any:
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_get_null_mask_card_number(input_data: str) -> Any:
    with pytest.raises(ValueError):
        get_mask_card_number("0000123456789000")


def test_get_upper_format_name_card_number(input_data: str) -> Any:
    with pytest.raises(ValueError):
        get_mask_card_number("VISA")


def test_get_uncorrect_name_card_number(input_data: str) -> Any:
    with pytest.raises(ValueError):
        get_mask_card_number("Счет 73654108430135874305")





@pytest.fixture
def user_data() -> list[str]:
    return ["Счет 64686473678894779589",
            "Счет 35383033474447895560",
            "Visa Platinum 8990922113665229",
            "Visa Gold 5999414228426353",
            "Счет 73654108430135874305",
            ]


@pytest.mark.parametrize("user_data, expected_mask", [
                        ("Счет 64686473678894779589", "Счет **9589"),
                        ("Счет 35383033474447895560", "Счет **5560"),
                        ("Счет 73654108430135874305", "Счет **4305"),
                        ])
def test_get_mask_account(user_data: str, expected_mask: str) -> Any:
    assert get_mask_account(user_data) == expected_mask


def test_get_mask_account_invalid_number(user_data: str) -> Any:
    with pytest.raises(ValueError):
        get_mask_account("12345678")


@pytest.mark.parametrize("user_data", [
                        (1831982476737658),
                        (12345),
                        (11098765),
                        (1158300734726758),
                         ])
def test_get_mask_account_wrong_type(user_data: str) -> Any:
    with pytest.raises(TypeError):
        get_mask_account(user_data)


@pytest.mark.parametrize("input_data, expected_mask", [
                        ("Visa Classic 6831982476737658",
                         "VisaClassic 6831 98** **** 7658"),
                        ("Visa Gold 5999414228426353",
                         "VisaGold 5999 41** **** 6353"),
                        ("Maestro 1596837868705199",
                         "Maestro 1596 83** **** 5199"),
                        ("Счет 35383033474447895560",
                         "Счет **5560"),
                        ("Счет 73654108430135874305",
                         "Счет **4305"),
                        ("MasterCard 7158300734726758",
                         "MasterCard 7158 30** **** 6758"),
                         ])
def test_mask_account_card(input_data: str, expected_mask: str) -> Any:
    assert mask_account_card(input_data) == expected_mask


@pytest.mark.parametrize("input_data", [
                        (6831982476737658),
                        (2345),
                        (1098765),
                        (7158300734726758),
                         ])
def test_mask_account_card_wrong_type(input_data: str) -> Any:
    with pytest.raises(TypeError):
        mask_account_card(input_data)



@pytest.mark.parametrize("input_data", [
                        (6831982476737658),
                        (2345),
                        (1098765),
                        (7158300734726758),
                         ])
def test_get_mask_card_number_wrong_type(input_data: str) -> Any:
    with pytest.raises(TypeError):
        get_mask_card_number(input_data)