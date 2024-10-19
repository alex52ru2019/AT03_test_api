# Напишите функцию, которая делает запрос к TheCatAPI для получения случайного изображения кошки. https://api.thecatapi.com/v1/images/search
# Напишите тест, который проверяет успешный запрос и возвращает правильный URL.
# Напишите тест, который проверяет неуспешный запрос (например, статус код 404) и возвращает None.

import requests

def get_cat():
    url = f'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

    # def get_cat_image(breed_id):
    #     url = f'https://api.thecatapi.com/v1/images/search?breed_ids={breed_id}'
    #     headers = {"x-api-key": THE_CAT_API_KEY}
    #     response = requests.get(url, headers=headers)
    #     data = response.json()
    #     return data[0]['url']