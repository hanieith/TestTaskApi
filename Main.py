import requests
import json
import logging.config

from settings import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')

API_LINK = 'https://wegfinder.at/api/v1/stations'


# Function for get address by coodrinates
def get_address(coordinates):
    try:
        response = requests.get(
            f'https://api.i-mobility.at/routing/api/v1/nearby_address?latitude={coordinates[1]}&longitude={coordinates[0]}')
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        return logger.exception(f'Error to get address: {error}')
    clean_data = json.loads(response.content)
    if clean_data == '???':
        logger.debug(f'Wrong address for {coordinates}')
        return 'Wrong coordinates'
    return clean_data['data']['name']


# Function for serialize data from api and add address
def serializer(data):
    coordinates = [data['longitude'], data['latitude']]
    try:
        clean_data = {
            'id': data['id'],
            'name': data['name'],
            'active': True if data['status'] == 'aktiv' else False,
            'description': data['description'],
            'boxes': data['boxes'],
            'free_boxes': data['free_boxes'],
            'free_bikes': data['free_bikes'],
            'free_ratio': round(data['free_boxes'] / data['free_bikes'], 2),
            'coordinates': coordinates,
            'address': get_address(coordinates),
        }
    except Exception as error:
        return logger.exception(f'Error with serializer: {error}')
    return clean_data

#Get data from api link
def get_data_from_api(API_LINK):
    try:
        response = requests.get(API_LINK)
        response.raise_for_status()
        logger.debug('Data from API received successfully')
        return response.content
    except requests.exceptions.RequestException as error:
        return logger.exception(f'Error to get data from API: {error}')


def get_stations_list(data):
    stations = json.loads(data)
    result = list()
    for station in stations:
        if station['free_bikes'] > 0:
            result.append(serializer(station))
    logger.debug('Data serialize successfully')
    data_sorted_by_name = sorted(result, key=lambda x: x['name'])
    data_sorted_by_free_bikes = sorted(data_sorted_by_name, reverse=True, key=lambda x: x['free_bikes'])
    return data_sorted_by_free_bikes


#
if __name__ == '__main__':
    for item in get_stations_list(get_data_from_api(API_LINK)):
        print(item, end='\n')
