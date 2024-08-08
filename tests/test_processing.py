from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def test_initial_list() -> list[dict[str, Any]]:
    return [{"id": 41428829, "state": "EXECUTED",
             "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "CANCELED",
             "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED",
             "date": "2018-09-12T21:27:25.241689"},
            {"id": 939719570, "state": "EXECUTED",
             "date": "2018-06-30T02:08:58.425572"},
            {"id": 616064591, "state": "FAILED",
             "date": "2022-02-24T08:21:33.419441"},
            {"id": 628064591, "state": "FAILED",
             "date": "2022-02-24T08:21:33.419441"},
            ]


@pytest.mark.parametrize("state, expected", [
    (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED",
                 "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED",
                 "date": "2018-06-30T02:08:58.425572"},
            ],
    ),
    (
        "FAILED",
        [
                {"id": 616064591, "state": "FAILED",
                 "date": "2022-02-24T08:21:33.419441"},
                {"id": 628064591, "state": "FAILED",
                 "date": "2022-02-24T08:21:33.419441"},
        ]
    )
])
def test_filter_by_state(test_initial_list: list[dict[str, Any]],
                         state: str, expected: list[dict[str, Any]]) -> Any:
    assert filter_by_state(test_initial_list, state) == expected


@pytest.mark.parametrize("state", [
    ("")
])
def test_filter_by_state_empty(test_initial_list: list[dict[str, Any]],
                               state: str) -> Any:
    with pytest.raises(ValueError):
        filter_by_state(test_initial_list, state)


@pytest.mark.parametrize("state", [(12345)])
def test_filter_by_state_wrong_type(test_initial_list: list[dict[str, Any]],
                                    state: str) -> Any:
    with pytest.raises(TypeError):
        filter_by_state(test_initial_list, state)


@pytest.mark.parametrize("reverse, expected", [
    (True, [
        {"id": 616064591, "state": "FAILED",
         "date": "2022-02-24T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED",
         "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED",
         "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED",
         "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED",
         "date": "2018-06-30T02:08:58.425572"},
    ]),
    (False, [
        {"id": 939719570, "state": "EXECUTED",
         "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED",
         "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED",
         "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED",
         "date": "2019-07-03T18:35:29.512364"},
        {"id": 616064591, "state": "FAILED",
         "date": "2022-02-24T08:21:33.419441"},
    ]),
])
def test_sort_by_date(test_initial_list: list[dict[str, Any]],
                      reverse: bool, expected: list[dict[str, Any]]) -> Any:
    assert sort_by_date(test_initial_list, reverse) == expected


@pytest.mark.parametrize("test_initial_list", [
    ([
       {"id": 939719570, "state": "EXECUTED", "date": 123345},
       {"id": 615064591, "state": "CANCELED", "date": [1234]},
      ],
     )
    ])
def test_sort_by_date_without_date(test_initial_list:
                                   list[dict[str, Any]]) -> Any:
    with pytest.raises(TypeError):
        sort_by_date(test_initial_list)


@pytest.mark.parametrize("test_initial_list", [
    ([
        "id939719570", "stateEXECUTED", "date2018-06-30T02:08:58.425572",
        "id342719570state:EXECUTED", "date: 2022-06-30T02:08:58.425572"
     ],
     )
    ])
def test_sort_by_date_wrong(test_initial_list: list[dict[str, Any]]) -> Any:
    with pytest.raises(TypeError):
        sort_by_date(test_initial_list)
