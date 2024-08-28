from unittest.mock import Mock
import pandas as pd

from unittest.mock import patch
from unittest.mock import mock_open

from src.import_file import transaction_from_csv
from src.import_file import transaction_from_excel


@patch('csv.reader')
def test_transaction_from_csv(mock_reader):
    m = mock_open()
    mock_reader.return_value = [{
            'id': '4234093',
            'state': 'EXECUTED',
            'date': '2021-07-08T07:31:21Z',
            'amount': '23182',
            'currency_name': 'Ruble',
            'currency_code': 'RUB'
        }]
    with patch('builtins.open', m) as mocked_open:
        assert transaction_from_csv('transaction.csv') == [{
            'id': '4234093',
            'state': 'EXECUTED',
            'date': '2021-07-08T07:31:21Z',
            'amount': '23182',
            'currency_name': 'Ruble',
            'currency_code': 'RUB'
            }]
        mocked_open.assert_called_with('transaction.csv', 'r', encoding='utf-8')
