import requests
from pprint import pprint
from datetime import datetime

DIRECTION_TRANSFORM = {
    'n': 'северное',
    'nne': 'северо - северо - восточное',
    'ne': 'северо - восточное',
    'ene': 'восточно - северо - восточное',
    'e': 'восточное',
    'ese': 'восточно - юго - восточное',
    'se': 'юго - восточное',
    'sse': 'юго - юго - восточное',
    's': 'южное',
    'ssw': 'юго - юго - западное',
    'sw': 'юго - западное',
    'wsw': 'западно - юго - западное',
    'w': 'западное',
    'wnw': 'западно - северо - западное',
    'nw': 'северо - западное',
    'nnw': 'северо - северо - западное',
    'c': 'штиль',
}


def yandex_current_weather(lat, lon):
    """
    Получение текущей погоды от Яндекс Погоды.
    """
    token = "be661674-56e4-454f-8050-bdce3a4dcb17"
    url = "https://api.weather.yandex.ru/v2/forecast"
    # Параметры для Яндекс API
    params = {
        'lat': lat,
        'lon': lon
    }
    headers = {
        'X-Yandex-API-Key': token
    }
    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    result = {
        'time': datetime.fromtimestamp(data['fact']['uptime']).strftime("%H:%M"),
        'temp': data['fact']['temp'],
        'feels_like_temp': data['fact']['feels_like'],
        'pressure': data['fact']['pressure_mm'],
        'humidity': data['fact']['humidity'],
        'wind_speed': data['fact']['wind_speed'],
        'wind_gust': data['fact']['wind_gust'],
        'wind_dir': DIRECTION_TRANSFORM.get(data['fact']['wind_dir'].lower()),
    }
    return result

if __name__ == "__main__":
     pprint(yandex_current_weather(59.93, 30.31))  # Проверка работы для координат Санкт-Петербурга
