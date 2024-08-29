from typing import Any

import pytest

from src.main import mask_account_card
from src.widget import get_date


@pytest.fixture
def input_data() -> list[str]:
    return ["Maestro 1596837868705199",
            "Account 64686473678894779589",
            "MasterCard 7158300734726758",
            "Account 35383033474447895560",
            "Visa Classic 6831982476737658",
            "Visa Platinum 8990922113665229",
            "Account 64686473678894779589",
            "Account 35383033474447895560",
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
                        ("Account 35383033474447895560",
                         "Account **5560"),
                        ("Account 73654108430135874305",
                         "Account **4305"),
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


@pytest.fixture
def time_data() -> list[str]:
    return ["2024-03-11T02:26:18.671407",
            "2022-02-14T02:20:11.687407",
            "2022-02-24T02:23:12.671407"
            ]


@pytest.mark.parametrize("time_data, expected", [
                        ("2024-03-11T02:26:18.671407", "11.03.2024"),
                        ("2022-02-14T02:20:11.687407", "14.02.2022"),
                        ("2022-02-24T02:23:12.671407", "24.02.2022"),
                        ])
def test_get_date(time_data: str, expected: str) -> Any:
    assert get_date(time_data) == expected


def test_invalid_get_date(time_data: str) -> Any:
    with pytest.raises(ValueError):
        get_date("1234545678T90000")


@pytest.mark.parametrize("time_data", [
                        (1831982476737658),
                        (12345),
                        (11098765),
                        (1158300734726758),
                         ])
def test_get_date_wrong_type(time_data: str) -> Any:
    with pytest.raises(TypeError):
        get_date(time_data)


def test_no_get_date(time_data: str) -> Any:
    with pytest.raises(ValueError):
        get_date("1234545678W900007893246789")
