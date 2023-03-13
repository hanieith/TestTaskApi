import pytest

from main import get_address, serializer, get_stations_list


@pytest.mark.parametrize("a, b, expected_result", [(16.330, 48.191, 'Reindorfgasse 39, Wien'),
                                                   (16.311770975589752, 48.21185884247232,
                                                    'U-Bahn Station Ottakring S, Wien'),
                                                   (16.36172588, 48.22585504, 'Julius-Tandler-Platz 7, Wien')])
def test_get_address_function(a, b, expected_result):
    assert get_address([a, b]) == expected_result


def test_serializer_function():
    enter_data = {'id': 109, 'name': 'Johannesgasse', 'status': 'aktiv',
                  'description': 'Parkring / Stadtpark beim Haupteingang des Kursalons', 'boxes': 20, 'free_boxes': 13,
                  'free_bikes': 6, 'longitude': 16.376719, 'latitude': 48.203366, 'internal_id': 1029}
    expected_data = {'id': 109, 'name': 'Johannesgasse', 'active': True,
                     'description': 'Parkring / Stadtpark beim Haupteingang des Kursalons', 'boxes': 20,
                     'free_boxes': 13,
                     'free_bikes': 6, 'free_ratio': 2.17, 'coordinates': [16.376719, 48.203366],
                     'address': 'Parkring 20, Wien'}
    assert serializer(enter_data) == expected_data


def test_get_stations_list():
    enter_data = b'[{"id":108,"name":"Friedrich Schmidtplatz","status":"aktiv","description":"Ecke Lichtenfelsgasse U2 Station Rathaus","boxes":24,"free_boxes":24,"free_bikes":0,"longitude":16.356581,"latitude":48.211433,"internal_id":1026},{"id":109,"name":"Johannesgasse","status":"aktiv","description":"Parkring / Stadtpark beim Haupteingang des Kursalons","boxes":20,"free_boxes":13,"free_bikes":6,"longitude":16.376719,"latitude":48.203366,"internal_id":1029},{"id":112,"name":"K\xc3\xa4rntner Ring","status":"aktiv","description":"Ecke Akademiestra\xc3\x9fe in der Mitte der beiden Einkaufszentren der Ringstra\xc3\x9fengalerien","boxes":16,"free_boxes":11,"free_bikes":5,"longitude":16.371317,"latitude":48.202157,"internal_id":1028}]\n'
    expected_data = [{'id': 109, 'name': 'Johannesgasse', 'active': True,
                      'description': 'Parkring / Stadtpark beim Haupteingang des Kursalons', 'boxes': 20,
                      'free_boxes': 13, 'free_bikes': 6, 'free_ratio': 2.17, 'coordinates': [16.376719, 48.203366],
                      'address': 'Parkring 20, Wien'},
                     {'id': 112, 'name': 'Kärntner Ring', 'active': True,
                                                        'description': 'Ecke Akademiestraße in der Mitte der beiden Einkaufszentren der Ringstraßengalerien',
                                                        'boxes': 16, 'free_boxes': 11, 'free_bikes':
                                                            5, 'free_ratio': 2.2, 'coordinates': [16.371317, 48.202157],
                                                        'address': 'Kärntner Ring 5-7, Wien'}]

    assert get_stations_list(enter_data) == expected_data
