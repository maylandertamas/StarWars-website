import requests


def get_planets_from_api(page_num):
    planets_data_needed_from_api = ['name', 'diameter', 'climate', 'terrain', 'surface_water', 'population' 'url']
    all_planet_data = []
    response = requests.get('http://swapi.co/api/planets/?page=' + str(page_num)).json()
    response = response['results']
    for dictionary in response:
        actual_planet_data = {}
        for key, value in dictionary.items():
            if key == 'url':
                if len(value) == 30:
                    planet_id = value[-2]
                else:
                    planet_id = value[-3:-1]
                actual_planet_data.update({'id': value})
            if key == 'name' or key == 'climate' or key == 'terrain' or key == 'population':
                actual_planet_data.update({key: value})
            if key == 'diameter':
                if value.isdigit():
                    diameter_in_km = str(int(value) / 1000)
                    actual_planet_data.update({key: diameter_in_km})
                else:
                    actual_planet_data.update({key: value})
            if key == 'surface_water':
                if not value.isdigit():
                    surface_water_percentage = value + '%'
                    actual_planet_data.update({key: surface_water_percentage})
                else:
                    actual_planet_data.update({key: value})

        all_planet_data.append(actual_planet_data)
    return all_planet_data
