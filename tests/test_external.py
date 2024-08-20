import json
import pytest

from unittest.mock import patch, MagicMock
from src.external_api import get_rate_exchange


@patch("requests.get")
def test_get_rate_exchange(mock_get):
	mock_response = MagicMock()
	mock_response.text = json.dumps({'info': {'rate': 90.82}})
	"""Настраиваю mock_get, чтобы он возвращал наш правильный но фиктивный ответ"""
	mock_get.return_value.json.return_value = mock_response
	"""Вызываю тестируемую функцию"""
	assert get_rate_exchange("USD", "GWXUgoP8ncjVagpxkWwJzrzksblrMRo8") == 90.82
