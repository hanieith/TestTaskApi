import requests
import json

response = requests.get('https://wegfinder.at/api/v1/stations')
stations = json.loads(response.content)

# Функция для получения адреса по API с помощью координат
def get_address(coordinates: list) -> str:
    response = requests.get(
        f'https://api.i-mobility.at/routing/api/v1/nearby_address?latitude={coordinates[1]}&longitude={coordinates[0]}')
    clean_data = json.loads(response.content)
    return clean_data['data']['name']


# Сериализатор для получения нужной  структуры
def serializer(data:dict) -> dict:
    coordinates = [data['longitude'], data['latitude']]
    clean_data = {
        'id': data['id'],
        'name': data['name'],
        'active': True if data['status'] == 'aktiv' else False,
        'description': data['description'],
        'boxes': data['boxes'],
        'free_boxes': data['free_boxes'],
        'free_bikes': data['free_bikes'],
        'free_ratio': round(data['free_boxes'] / data['free_bikes'] if data['free_bikes'] > 0 else 0, 2),
        'coordinates': coordinates,
        'address': get_address(coordinates),
    }
    return clean_data


# Получение списка станций, проверка на нулевое количество bikes и сортировка по имени и по количеству свободных bikes
def get_station_list() -> list:
    result = list()
    for station in stations:
        if station['free_bikes'] > 0:
            result.append(serializer(station))
    return sorted(sorted(result, key=lambda x: x['name']), reverse=True, key=lambda x: x['free_bikes'])


# Вывод для откладки кода
if __name__ == '__main__':
    for _ in get_station_list():
        print(_, sep='/n')
