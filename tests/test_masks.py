from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def input_data() -> list[str]:
    return ["Maestro 1596837868705199",
            "Account 64686473678894779589",
            "MasterCard 7158300734726758",
            "Account 35383033474447895560",
            "Visa Classic 6831982476737658",
            "Visa Platinum 8990922113665229",
            "Visa Gold 5999414228426353",
            "Account 73654108430135874305",
            ]


@pytest.mark.parametrize("input_data, expected_mask", [
                        ("Visa Classic 6831982476737658",
                         "VisaClassic 6831 98** **** 7658"),
                        ("Visa Gold 5999414228426353",
                         "VisaGold 5999 41** **** 6353"),
                        ("Maestro 1596837868705199",
                         "Maestro 1596 83** **** 5199"),
                        ("MasterCard 7158300734726758",
                         "MasterCard 7158 30** **** 6758"),
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
        get_mask_card_number("Account 73654108430135874305")


@pytest.mark.parametrize("input_data", [
                        (6831982476737658),
                        (2345),
                        (1098765),
                        (7158300734726758),
                         ])
def test_get_mask_card_number_wrong_type(input_data: str) -> Any:
    with pytest.raises(TypeError):
        get_mask_card_number(input_data)


@pytest.fixture
def user_data() -> list[str]:
    return ["Account 64686473678894779589",
            "Account 35383033474447895560",
            "Visa Platinum 8990922113665229",
            "Visa Gold 5999414228426353",
            "Account 73654108430135874305",
            ]


@pytest.mark.parametrize("user_data, expected_mask", [
                        ("Account 64686473678894779589", "Account **9589"),
                        ("Account 35383033474447895560", "Account **5560"),
                        ("Account 73654108430135874305", "Account **4305"),
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
