from src.import_file import transactions_from_csvExcel
from unittest.mock import patch


@patch('src.import_file.pd.read_excel')
def test_correct_transactions(mock_read, test_df):
    """Проверка корректности чтения и вывода файла"""
    mock_read.return_value = test_df
    assert transactions_from_csvExcel('..\\data\\transactions_excel.xlsx') == test_df.to_dict(
        orient='records')


def test_transaction_with_incorrect_path():
    """Проверка работы функции с пустым путём до файла"""
    assert transactions_from_csvExcel("") == []
