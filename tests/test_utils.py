import pytest
from src.utils import get_data_about_transactions

def test_get_data_about_transactions():
	"""тест на пустой список"""
	assert get_data_about_transactions("[]")==[]


def test_get_data_about_transactions_wrong():
	"""тест на неправильный путь"""
	assert get_data_about_transactions(path_to_file="..\\main\\operations.json")==[]


