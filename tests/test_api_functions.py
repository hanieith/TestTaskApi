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
    enter_data = b'[{"id":108,"name":"Friedrich Schmidtplatz","status":"aktiv","description":"Ecke Lichtenfelsgasse U2 Station Rathaus","boxes":24,"free_boxes":24,"free_bikes":0,"longitude":16.356581,"latitude":48.211433,"internal_id":1026},{"id":109,"name":"Johannesgasse","status":"aktiv","description":"Parkring / Stadtpark beim Haupteingang des Kursalons","boxes":20,"free_boxes":13,"free_bikes":6,"longitude":16.376719,"latitude":48.203366,"internal_id":1029},{"id":112,"name":"K\xc3\xa4rntner Ring","status":"aktiv","description":"Ecke Akademiestra\xc3\x9fe in der Mitte der beiden Einkaufszentren der Ringstra\xc3\x9fengalerien","boxes":16,"free_boxes":11,"free_bikes":5,"longitude":16.371317,"latitude":48.202157,"internal_id":1028},{"id":110,"name":"Rathausplatz","status":"aktiv","description":"Universit\xc3\xa4tsring gegen\xc3\xbcber des Burgtheaters","boxes":20,"free_boxes":20,"free_bikes":0,"longitude":16.36025,"latitude":48.209921,"internal_id":1027},{"id":103,"name":"Schottenring U4","status":"aktiv","description":"Franz-Josefs-Kai / Ringturm / H\xc3\xb6he Werdertorgasse U4 Station Schottenring beim Ausgang Salztorbr\xc3\xbccke","boxes":21,"free_boxes":16,"free_bikes":5,"longitude":16.372222,"latitude":48.215964,"internal_id":1020},{"id":104,"name":"Schwedenplatz","status":"aktiv","description":"Franz-Josefs-Kai / Rotenturmstra\xc3\x9fe bei der U-Bahnstation Schwedenplatz - Ausgang Rotenturmstra\xc3\x9fe","boxes":30,"free_boxes":29,"free_bikes":1,"longitude":16.376655,"latitude":48.211699,"internal_id":1023},{"id":101,"name":"Singerstra\xc3\x9fe","status":"aktiv","description":"Singerstra\xc3\x9fe vor Hausnummer 2","boxes":22,"free_boxes":9,"free_bikes":12,"longitude":16.372136949390438,"latitude":48.20782938971974,"internal_id":1030},{"id":106,"name":"Stadtpark Stubenring","status":"aktiv","description":"Parkring / Weiskirchner Str. / Stadtpark gegen\xc3\xbcber dem Museum f\xc3\xbcr Angewandte Kunst","boxes":20,"free_boxes":17,"free_bikes":1,"longitude":16.380446122684475,"latitude":48.20682045864029,"internal_id":1024},{"id":113,"name":"Universit\xc3\xa4tsring","status":"aktiv","description":"gegen\xc3\xbcber ONr. 6","boxes":38,"free_boxes":19,"free_bikes":19,"longitude":16.360787,"latitude":48.21192,"internal_id":1134},{"id":102,"name":"Wallnerstra\xc3\x9fe","status":"aktiv","description":"Ecke Fahnengasse U3 Station Herrengasse vor dem Ausgang Fahnengasse","boxes":27,"free_boxes":1,"free_bikes":25,"longitude":16.36668681481933,"latitude":48.2097240924198,"internal_id":1021},{"id":201,"name":"Heinestra\xc3\x9fe","status":"aktiv","description":"U-Bahn Aufgang Heinestra\xc3\x9fe","boxes":38,"free_boxes":20,"free_bikes":18,"longitude":16.390280334987665,"latitude":48.21845439674175,"internal_id":1069},{"id":207,"name":"Messeplatz","status":"aktiv","description":"Messeplatz","boxes":40,"free_boxes":18,"free_bikes":20,"longitude":16.406171,"latitude":48.217296,"internal_id":1080},{"id":202,"name":"Nepomukgasse","status":"aktiv","description":"Nestroyplatz U1","boxes":15,"free_boxes":5,"free_bikes":10,"longitude":16.38621,"latitude":48.215878,"internal_id":1065},{"id":204,"name":"Obere Donaustra\xc3\x9fe","status":"aktiv","description":"Obere Donaustra\xc3\x9fe Ecke Herminengasse, U2 Schottenring Ausgang Herminengasse","boxes":20,"free_boxes":13,"free_bikes":7,"longitude":16.373086273670197,"latitude":48.21777468054901,"internal_id":1077},{"id":206,"name":"Praterstern","status":"aktiv","description":"Praterstern Schnellbahnunterf\xc3\xbchrung","boxes":40,"free_boxes":28,"free_bikes":12,"longitude":16.392030715942383,"latitude":48.217831869605355,"internal_id":1086},{"id":212,"name":"Radingerstra\xc3\x9fe","status":"aktiv","description":"Lassallestra\xc3\x9fe vor 9","boxes":33,"free_boxes":4,"free_bikes":29,"longitude":16.399790024753543,"latitude":48.223183193262095,"internal_id":1142},{"id":209,"name":"Stadion Center","status":"aktiv","description":"Meiereistra\xc3\x9fe/Vorgartenstra\xc3\x9fe, Unter U2 Stadion","boxes":40,"free_boxes":2,"free_bikes":38,"longitude":16.421406,"latitude":48.209983,"internal_id":1082},{"id":307,"name":"Kundmanngasse","status":"aktiv","description":"Kundmanngasse vor 2","boxes":27,"free_boxes":9,"free_bikes":18,"longitude":16.39601008933255,"latitude":48.20568564112994,"internal_id":1105},{"id":311,"name":"Petrusgasse","status":"aktiv","description":"Landstra\xc3\x9fer Hauptstra\xc3\x9fe vor 146","boxes":28,"free_boxes":10,"free_bikes":18,"longitude":16.398464284091915,"latitude":48.19298666107499,"internal_id":1127},{"id":313,"name":"Wien Mitte","status":"aktiv","description":"Landstra\xc3\x9fer Hauptstra\xc3\x9fe vor 2B, an der Kreuzung Invalidenstra\xc3\x9fe","boxes":28,"free_boxes":20,"free_bikes":8,"longitude":16.385247276821133,"latitude":48.20585160205631,"internal_id":1128},{"id":402,"name":"Mayerhofgasse","status":"aktiv","description":"Wiedner Hauptstra\xc3\x9fe vor 49","boxes":19,"free_boxes":19,"free_bikes":0,"longitude":16.36707037105566,"latitude":48.192882761349345,"internal_id":1104},{"id":403,"name":"Sankt-Elisabeth-Platz","status":"aktiv","description":"Sankt-Elisabeth-Platz gegen\xc3\xbcber 1","boxes":21,"free_boxes":21,"free_bikes":0,"longitude":16.37566685094839,"latitude":48.190857735513326,"internal_id":1125},{"id":401,"name":"Treitlstra\xc3\x9fe","status":"aktiv","description":"Vor der TU-Bibliothek, U-Bahn Karlsplatz","boxes":20,"free_boxes":16,"free_bikes":4,"longitude":16.36822705522536,"latitude":48.19987078817638,"internal_id":1067},{"id":502,"name":"Falco Stiege","status":"aktiv","description":"Kettenbr\xc3\xbcckengasse U4 Station Kettenbr\xc3\xbcckengasse - Ausgang Eggerthgasse","boxes":17,"free_boxes":16,"free_bikes":0,"longitude":16.357409,"latitude":48.19636,"internal_id":1042},{"id":501,"name":"Pilgramgasse U4","status":"aktiv","description":"Rechte Wienzeile gegen\xc3\xbcber 85 U4 Station Pilgramgasse","boxes":21,"free_boxes":16,"free_bikes":5,"longitude":16.354877331929174,"latitude":48.19305411244311,"internal_id":1041},{"id":505,"name":"Reinprechtsdorfer Br\xc3\xbccke","status":"aktiv","description":"Rechte Wienzeile Ecke Reinprechtsdorferstra\xc3\x9fe","boxes":20,"free_boxes":19,"free_bikes":0,"longitude":16.351027,"latitude":48.189527,"internal_id":1056},{"id":507,"name":"Siebenbrunnenplatz","status":"aktiv","description":"Siebenbrunnenplatz vor 5","boxes":26,"free_boxes":7,"free_bikes":19,"longitude":16.3530230023689,"latitude":48.18527731094403,"internal_id":1107},{"id":601,"name":"Kollergerngasse","status":"aktiv","description":"Mariahilferstra\xc3\x9fe Ecke Kollergerngasse","boxes":20,"free_boxes":9,"free_bikes":9,"longitude":16.350918,"latitude":48.198527,"internal_id":1068},{"id":702,"name":"Burggasse U6","status":"aktiv","description":"Neubaug\xc3\xbcrtel / Burggasse U6 Station Burggasse - Ausgang Burggasse","boxes":20,"free_boxes":16,"free_bikes":3,"longitude":16.3374263048172,"latitude":48.20367562940292,"internal_id":1044},{"id":701,"name":"Museumsplatz","status":"aktiv","description":"Mariahilfer Stra\xc3\x9fe / Museumsquartier U2 Station Museumsquartier","boxes":36,"free_boxes":9,"free_bikes":25,"longitude":16.361115244214943,"latitude":48.20234525336636,"internal_id":1032},{"id":703,"name":"Schottenfeldgasse","status":"aktiv","description":"vor der Kirche bei Lerchenfelderstra\xc3\x9fe","boxes":27,"free_boxes":24,"free_bikes":0,"longitude":16.343241,"latitude":48.207249,"internal_id":1045},{"id":705,"name":"Siebensternplatz","status":"aktiv","description":"Siebensterngasse vor 38 - 40","boxes":19,"free_boxes":19,"free_bikes":0,"longitude":16.352420579202636,"latitude":48.202220666649325,"internal_id":1076},{"id":802,"name":"Albertgasse","status":"aktiv","description":"Albertgasse vor 28, nahe Kreuzung Josefst\xc3\xa4dter Stra\xc3\x9fe","boxes":32,"free_boxes":26,"free_bikes":5,"longitude":16.344066730857776,"latitude":48.21053857454122,"internal_id":1140},{"id":902,"name":"Julius-Tandler-Platz","status":"aktiv","description":"Nordbergstra\xc3\x9fe Franz Josefs Bahnhof","boxes":16,"free_boxes":13,"free_bikes":3,"longitude":16.36172588,"latitude":48.22585504,"internal_id":1034},{"id":909,"name":"Markthalle Alsergrund","status":"aktiv","description":"Nu\xc3\x9fdorferstra\xc3\x9fe vor 22","boxes":24,"free_boxes":15,"free_bikes":8,"longitude":16.35486246350276,"latitude":48.2251402686428,"internal_id":1106},{"id":903,"name":"Ro\xc3\x9fauer L\xc3\xa4nde U4","status":"aktiv","description":"U4 Station Rossauer L\xc3\xa4nde - Ausgang Nordwest","boxes":28,"free_boxes":23,"free_bikes":5,"longitude":16.367440223693848,"latitude":48.22274274152399,"internal_id":1035},{"id":907,"name":"Sensengasse","status":"aktiv","description":"Sensengasse 1 nahe Spitalgasse","boxes":20,"free_boxes":16,"free_bikes":3,"longitude":16.352464109659195,"latitude":48.21931648931047,"internal_id":1094},{"id":901,"name":"Sigmund Freud Park","status":"aktiv","description":"W\xc3\xa4hringerstra\xc3\x9fe Ecke Universit\xc3\xa4tsstra\xc3\x9fe / Votivkirche Im Park zwischen der Votivkirche und dem Schottentor","boxes":36,"free_boxes":31,"free_bikes":5,"longitude":16.361394,"latitude":48.214592,"internal_id":1022},{"id":1001,"name":"Hauptbahnhof West","status":"aktiv","description":"neben dem Busbahnhof in der Unterf\xc3\xbchrung","boxes":40,"free_boxes":4,"free_bikes":36,"longitude":16.3740655721665,"latitude":48.185165595330574,"internal_id":1143},{"id":1201,"name":"L\xc3\xa4ngenfeldgasse","status":"aktiv","description":"U-Bahn Ausgang Storchensteg","boxes":25,"free_boxes":7,"free_bikes":17,"longitude":16.333931,"latitude":48.184268,"internal_id":1071},{"id":1301,"name":"Sch\xc3\xb6nbrunn Haupteingang","status":"aktiv","description":"Schlo\xc3\x9f Sch\xc3\xb6nbrunn gegen\xc3\xbcber Haupteingang","boxes":40,"free_boxes":17,"free_bikes":22,"longitude":16.31269962155625,"latitude":48.18720003399649,"internal_id":1075},{"id":1508,"name":"Meiselmarkt","status":"aktiv","description":"Johnstra\xc3\x9fe gegen\xc3\xbcber 61","boxes":28,"free_boxes":4,"free_bikes":24,"longitude":16.31897807121277,"latitude":48.19836424256149,"internal_id":1095},{"id":1503,"name":"Sch\xc3\xb6nbrunner Br\xc3\xbccke","status":"aktiv","description":"direkt auf der Br\xc3\xbccke","boxes":16,"free_boxes":15,"free_bikes":1,"longitude":16.319898,"latitude":48.185866,"internal_id":1074},{"id":1514,"name":"Westbahnhof Felberstra\xc3\x9fe","status":"aktiv","description":"Felbersta\xc3\x9fe vor 1","boxes":40,"free_boxes":23,"free_bikes":17,"longitude":16.33772000670433,"latitude":48.1979628716984,"internal_id":1129},{"id":1601,"name":"Josefst\xc3\xa4dter Stra\xc3\x9fe U6","status":"aktiv","description":"\xc3\x84usserer Hernalser G\xc3\xbcrtel U6 Station Josefst\xc3\xa4dterstra\xc3\x9fe","boxes":26,"free_boxes":23,"free_bikes":2,"longitude":16.339110008598254,"latitude":48.212107897872485,"internal_id":1039},{"id":1605,"name":"Ottakring U3","status":"aktiv","description":"Paltaufgasse gg\xc3\xbc. 16","boxes":39,"free_boxes":35,"free_bikes":4,"longitude":16.311770975589752,"latitude":48.21185884247232,"internal_id":1114},{"id":1803,"name":"Michelbeuern","status":"aktiv","description":"W\xc3\xa4hringer G\xc3\xbcrtel vor 40 Ecke Kreuzgasse","boxes":31,"free_boxes":9,"free_bikes":21,"longitude":16.343716084957123,"latitude":48.221818861642916,"internal_id":1097},{"id":2003,"name":"Hellwagstra\xc3\x9fe","status":"aktiv","description":"Meldemannstra\xc3\x9fe 26 Ecke Hellwagstra\xc3\x9fe","boxes":30,"free_boxes":20,"free_bikes":8,"longitude":16.380315,"latitude":48.237464,"internal_id":1083}]\n'
    expected_data = [{'id': 209, 'name': 'Stadion Center', 'active': True, 'description': 'Meiereistraße/Vorgartenstraße, Unter U2 Stadion', 'boxes': 40, 'free_boxes': 2, 'free_bikes': 38, 'free_ratio': 0.05, 'coordinates': [16.421406, 48.209983], 'address': 'Olympiaplatz 2, Wien'}, {'id': 1001, 'name': 'Hauptbahnhof West', 'active': True, 'description': 'neben dem Busbahnhof in der Unterführung', 'boxes': 40, 'free_boxes': 4, 'free_bikes': 36, 'free_ratio': 0.11, 'coordinates': [16.3740655721665, 48.185165595330574], 'address': 'Südtiroler Platz 12, Wien'}, {'id': 212, 'name': 'Radingerstraße', 'active': True, 'description': 'Lassallestraße vor 9', 'boxes': 33, 'free_boxes': 4, 'free_bikes': 29, 'free_ratio': 0.14, 'coordinates': [16.399790024753543, 48.223183193262095], 'address': 'Lassallestraße 9B, Wien'}, {'id': 701, 'name': 'Museumsplatz', 'active': True, 'description': 'Mariahilfer Straße / Museumsquartier U2 Station Museumsquartier', 'boxes': 36, 'free_boxes': 9, 'free_bikes': 25, 'free_ratio': 0.36, 'coordinates': [16.361115244214943, 48.20234525336636], 'address': 'Mariahilfer Straße 1, Wien'}, {'id': 102, 'name': 'Wallnerstraße', 'active': True, 'description': 'Ecke Fahnengasse U3 Station Herrengasse vor dem Ausgang Fahnengasse', 'boxes': 27, 'free_boxes': 1, 'free_bikes': 25, 'free_ratio': 0.04, 'coordinates': [16.36668681481933, 48.2097240924198], 'address': 'Wallnerstraße 6, Wien'}, {'id': 1508, 'name': 'Meiselmarkt', 'active': True, 'description': 'Johnstraße gegenüber 61', 'boxes': 28, 'free_boxes': 4, 'free_bikes': 24, 'free_ratio': 0.17, 'coordinates': [16.31897807121277, 48.19836424256149], 'address': 'Johnstraße 42, Wien'}, {'id': 1301, 'name': 'Schönbrunn Haupteingang', 'active': True, 'description': 'Schloß Schönbrunn gegenüber Haupteingang', 'boxes': 40, 'free_boxes': 17, 'free_bikes': 22, 'free_ratio': 0.77, 'coordinates': [16.31269962155625, 48.18720003399649], 'address': 'Schönbrunner Schloßbrücke 1302, Wien'}, {'id': 1803, 'name': 'Michelbeuern', 'active': True, 'description': 'Währinger Gürtel vor 40 Ecke Kreuzgasse', 'boxes': 31, 'free_boxes': 9, 'free_bikes': 21, 'free_ratio': 0.43, 'coordinates': [16.343716084957123, 48.221818861642916], 'address': 'Währinger Gürtel 40, Wien'}, {'id': 207, 'name': 'Messeplatz', 'active': True, 'description': 'Messeplatz', 'boxes': 40, 'free_boxes': 18, 'free_bikes': 20, 'free_ratio': 0.9, 'coordinates': [16.406171, 48.217296], 'address': 'Messeplatz 1, Wien'}, {'id': 507, 'name': 'Siebenbrunnenplatz', 'active': True, 'description': 'Siebenbrunnenplatz vor 5', 'boxes': 26, 'free_boxes': 7, 'free_bikes': 19, 'free_ratio': 0.37, 'coordinates': [16.3530230023689, 48.18527731094403], 'address': 'Siebenbrunnenplatz 5, Wien'}, {'id': 113, 'name': 'Universitätsring', 'active': True, 'description': 'gegenüber ONr. 6', 'boxes': 38, 'free_boxes': 19, 'free_bikes': 19, 'free_ratio': 1.0, 'coordinates': [16.360787, 48.21192], 'address': 'Universitätsring 6, Wien'}, {'id': 201, 'name': 'Heinestraße', 'active': True, 'description': 'U-Bahn Aufgang Heinestraße', 'boxes': 38, 'free_boxes': 20, 'free_bikes': 18, 'free_ratio': 1.11, 'coordinates': [16.390280334987665, 48.21845439674175], 'address': 'Heinestraße 42, Wien'}, {'id': 307, 'name': 'Kundmanngasse', 'active': True, 'description': 'Kundmanngasse vor 2', 'boxes': 27, 'free_boxes': 9, 'free_bikes': 18, 'free_ratio': 0.5, 'coordinates': [16.39601008933255, 48.20568564112994], 'address': 'Kundmanngasse 2, Wien'}, {'id': 311, 'name': 'Petrusgasse', 'active': True, 'description': 'Landstraßer Hauptstraße vor 146', 'boxes': 28, 'free_boxes': 10, 'free_bikes': 18, 'free_ratio': 0.56, 'coordinates': [16.398464284091915, 48.19298666107499], 'address': 'Landstraßer Hauptstraße 147, Wien'}, {'id': 1201, 'name': 'Längenfeldgasse', 'active': True, 'description': 'U-Bahn Ausgang Storchensteg', 'boxes': 25, 'free_boxes': 7, 'free_bikes': 17, 'free_ratio': 0.41, 'coordinates': [16.333931, 48.184268], 'address': 'U-Bahn Station Längenfeldgasse, Wien'}, {'id': 1514, 'name': 'Westbahnhof Felberstraße', 'active': True, 'description': 'Felberstaße vor 1', 'boxes': 40, 'free_boxes': 23, 'free_bikes': 17, 'free_ratio': 1.35, 'coordinates': [16.33772000670433, 48.1979628716984], 'address': 'Felberstraße 4, Wien'}, {'id': 206, 'name': 'Praterstern', 'active': True, 'description': 'Praterstern Schnellbahnunterführung', 'boxes': 40, 'free_boxes': 28, 'free_bikes': 12, 'free_ratio': 2.33, 'coordinates': [16.392030715942383, 48.217831869605355], 'address': 'U-Bahn Station Praterstern U, Wien'}, {'id': 101, 'name': 'Singerstraße', 'active': True, 'description': 'Singerstraße vor Hausnummer 2', 'boxes': 22, 'free_boxes': 9, 'free_bikes': 12, 'free_ratio': 0.75, 'coordinates': [16.372136949390438, 48.20782938971974], 'address': 'Singerstraße 2, Wien'}, {'id': 202, 'name': 'Nepomukgasse', 'active': True, 'description': 'Nestroyplatz U1', 'boxes': 15, 'free_boxes': 5, 'free_bikes': 10, 'free_ratio': 0.5, 'coordinates': [16.38621, 48.215878], 'address': 'Nepomukgasse 4, Wien'}, {'id': 601, 'name': 'Kollergerngasse', 'active': True, 'description': 'Mariahilferstraße Ecke Kollergerngasse', 'boxes': 20, 'free_boxes': 9, 'free_bikes': 9, 'free_ratio': 1.0, 'coordinates': [16.350918, 48.198527], 'address': 'Mariahilfer Straße 71, Wien'}, {'id': 2003, 'name': 'Hellwagstraße', 'active': True, 'description': 'Meldemannstraße 26 Ecke Hellwagstraße', 'boxes': 30, 'free_boxes': 20, 'free_bikes': 8, 'free_ratio': 2.5, 'coordinates': [16.380315, 48.237464], 'address': 'Hellwagstraße 13, Wien'}, {'id': 909, 'name': 'Markthalle Alsergrund', 'active': True, 'description': 'Nußdorferstraße vor 22', 'boxes': 24, 'free_boxes': 15, 'free_bikes': 8, 'free_ratio': 1.88, 'coordinates': [16.35486246350276, 48.2251402686428], 'address': 'Nußdorfer Straße 22, Wien'}, {'id': 313, 'name': 'Wien Mitte', 'active': True, 'description': 'Landstraßer Hauptstraße vor 2B, an der Kreuzung Invalidenstraße', 'boxes': 28, 'free_boxes': 20, 'free_bikes': 8, 'free_ratio': 2.5, 'coordinates': [16.385247276821133, 48.20585160205631], 'address': 'Landstraßer Hauptstraße 1D, Wien'}, {'id': 204, 'name': 'Obere Donaustraße', 'active': True, 'description': 'Obere Donaustraße Ecke Herminengasse, U2 Schottenring Ausgang Herminengasse', 'boxes': 20, 'free_boxes': 13, 'free_bikes': 7, 'free_ratio': 1.86, 'coordinates': [16.373086273670197, 48.21777468054901], 'address': 'Obere Donaustraße 59, Wien'}, {'id': 109, 'name': 'Johannesgasse', 'active': True, 'description': 'Parkring / Stadtpark beim Haupteingang des Kursalons', 'boxes': 20, 'free_boxes': 13, 'free_bikes': 6, 'free_ratio': 2.17, 'coordinates': [16.376719, 48.203366], 'address': 'Parkring 20, Wien'}, {'id': 802, 'name': 'Albertgasse', 'active': True, 'description': 'Albertgasse vor 28, nahe Kreuzung Josefstädter Straße', 'boxes': 32, 'free_boxes': 26, 'free_bikes': 5, 'free_ratio': 5.2, 'coordinates': [16.344066730857776, 48.21053857454122], 'address': 'Albertgasse 25, Wien'}, {'id': 112, 'name': 'Kärntner Ring', 'active': True, 'description': 'Ecke Akademiestraße in der Mitte der beiden Einkaufszentren der Ringstraßengalerien', 'boxes': 16, 'free_boxes': 11, 'free_bikes': 5, 'free_ratio': 2.2, 'coordinates': [16.371317, 48.202157], 'address': 'Kärntner Ring 5-7, Wien'}, {'id': 501, 'name': 'Pilgramgasse U4', 'active': True, 'description': 'Rechte Wienzeile gegenüber 85 U4 Station Pilgramgasse', 'boxes': 21, 'free_boxes': 16, 'free_bikes': 5, 'free_ratio': 3.2, 'coordinates': [16.354877331929174, 48.19305411244311], 'address': 'Rechte Wienzeile 87, Wien'}, {'id': 903, 'name': 'Roßauer Lände U4', 'active': True, 'description': 'U4 Station Rossauer Lände - Ausgang Nordwest', 'boxes': 28, 'free_boxes': 23, 'free_bikes': 5, 'free_ratio': 4.6, 'coordinates': [16.367440223693848, 48.22274274152399], 'address': 'U-Bahn Station Roßauer Lände, Wien'}, {'id': 103, 'name': 'Schottenring U4', 'active': True, 'description': 'Franz-Josefs-Kai / Ringturm / Höhe Werdertorgasse U4 Station Schottenring beim Ausgang Salztorbrücke', 'boxes': 21, 'free_boxes': 16, 'free_bikes': 5, 'free_ratio': 3.2, 'coordinates': [16.372222, 48.215964], 'address': 'Schanzelufer L, Wien'}, {'id': 901, 'name': 'Sigmund Freud Park', 'active': True, 'description': 'Währingerstraße Ecke Universitätsstraße / Votivkirche Im Park zwischen der Votivkirche und dem Schottentor', 'boxes': 36, 'free_boxes': 31, 'free_bikes': 5, 'free_ratio': 6.2, 'coordinates': [16.361394, 48.214592], 'address': 'Währinger Straße 2-4, Wien'}, {'id': 1605, 'name': 'Ottakring U3', 'active': True, 'description': 'Paltaufgasse ggü. 16', 'boxes': 39, 'free_boxes': 35, 'free_bikes': 4, 'free_ratio': 8.75, 'coordinates': [16.311770975589752, 48.21185884247232], 'address': 'U-Bahn Station Ottakring S, Wien'}, {'id': 401, 'name': 'Treitlstraße', 'active': True, 'description': 'Vor der TU-Bibliothek, U-Bahn Karlsplatz', 'boxes': 20, 'free_boxes': 16, 'free_bikes': 4, 'free_ratio': 4.0, 'coordinates': [16.36822705522536, 48.19987078817638], 'address': 'Treitlstraße 2, Wien'}, {'id': 702, 'name': 'Burggasse U6', 'active': True, 'description': 'Neubaugürtel / Burggasse U6 Station Burggasse - Ausgang Burggasse', 'boxes': 20, 'free_boxes': 16, 'free_bikes': 3, 'free_ratio': 5.33, 'coordinates': [16.3374263048172, 48.20367562940292], 'address': 'Neubaugürtel 52, Wien'}, {'id': 902, 'name': 'Julius-Tandler-Platz', 'active': True, 'description': 'Nordbergstraße Franz Josefs Bahnhof', 'boxes': 16, 'free_boxes': 13, 'free_bikes': 3, 'free_ratio': 4.33, 'coordinates': [16.36172588, 48.22585504], 'address': 'Julius-Tandler-Platz 7, Wien'}, {'id': 907, 'name': 'Sensengasse', 'active': True, 'description': 'Sensengasse 1 nahe Spitalgasse', 'boxes': 20, 'free_boxes': 16, 'free_bikes': 3, 'free_ratio': 5.33, 'coordinates': [16.352464109659195, 48.21931648931047], 'address': 'Sensengasse 1, Wien'}, {'id': 1601, 'name': 'Josefstädter Straße U6', 'active': True, 'description': 'Äusserer Hernalser Gürtel U6 Station Josefstädterstraße', 'boxes': 26, 'free_boxes': 23, 'free_bikes': 2, 'free_ratio': 11.5, 'coordinates': [16.339110008598254, 48.212107897872485], 'address': 'Hernalser Gürtel 1, Wien'}, {'id': 104, 'name': 'Schwedenplatz', 'active': True, 'description': 'Franz-Josefs-Kai / Rotenturmstraße bei der U-Bahnstation Schwedenplatz - Ausgang Rotenturmstraße', 'boxes': 30, 'free_boxes': 29, 'free_bikes': 1, 'free_ratio': 29.0, 'coordinates': [16.376655, 48.211699], 'address': 'Franz-Josefs-Kai 21, Wien'}, {'id': 1503, 'name': 'Schönbrunner Brücke', 'active': True, 'description': 'direkt auf der Brücke', 'boxes': 16, 'free_boxes': 15, 'free_bikes': 1, 'free_ratio': 15.0, 'coordinates': [16.319898, 48.185866], 'address': 'Schönbrunner Brücke 1221, Wien'}, {'id': 106, 'name': 'Stadtpark Stubenring', 'active': True, 'description': 'Parkring / Weiskirchner Str. / Stadtpark gegenüber dem Museum für Angewandte Kunst', 'boxes': 20, 'free_boxes': 17, 'free_bikes': 1, 'free_ratio': 17.0, 'coordinates': [16.380446122684475, 48.20682045864029], 'address': 'Parkring 2, Wien'}]
    assert get_stations_list(enter_data) == expected_data