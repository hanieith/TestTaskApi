import requests
import json

response = requests.get('https://wegfinder.at/api/v1/stations')
stations = json.loads(response.content)


def get_address(coordinates):
    response = requests.get(
        f'https://api.i-mobility.at/routing/api/v1/nearby_address?latitude={coordinates[1]}&longitude={coordinates[0]}')
    clean_data = json.loads(response.content)
    return clean_data['data']['name']


def serializer(data):
    coordinates = [data['longitude'], data['latitude']]
    clean_data = {
        'id': data['id'],
        'name': data['name'],
        'active': True if data['status'] == 'aktiv' else False,
        'description': data['description'],
        'boxes': data['boxes'],
        'free_boxes': data['free_boxes'],
        'free_bikes': data['free_bikes'],
        'free_ratio': data['free_boxes'] / data['free_bikes'] if data['free_bikes'] > 0 else 0,
        'coordinates': coordinates,
        'address': get_address(coordinates),
    }
    return clean_data


def main():
    result = list()
    for station in stations:
        if station['free_bikes'] > 0:
            result.append(serializer(station))
    return sorted(result, reverse=True, key=lambda x: x['free_bikes'])

for _ in main():
    print(_, sep='/n')