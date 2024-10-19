# Напишите функцию, которая делает запрос к TheCatAPI для получения случайного изображения кошки. https://api.thecatapi.com/v1/images/search
# Напишите тест, который проверяет успешный запрос и возвращает правильный URL.
# Напишите тест, который проверяет неуспешный запрос (например, статус код 404) и возвращает None.

import pytest
from main_dz import get_cat

def test_get_cat(mocker):
    mock_get = mocker.patch('main_dz.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'url': 'https://example.com/cat.jpg'
    }

    cat_data = get_cat()
    assert cat_data == {
        'url': 'https://example.com/cat.jpg'
    }

def test_get_cat_err(mocker):
    mock_get = mocker.patch('main_dz.requests.get')
    mock_get.return_value.status_code = 404
    cat_data = get_cat()
    assert cat_data == None