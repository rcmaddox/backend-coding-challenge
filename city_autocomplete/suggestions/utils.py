from geopy.distance import great_circle

def calculate_score(city, query, latitude, longitude):
    name_score = len(query) / len(city.name)
    if latitude and longitude:
        distance = great_circle((city.latitude, city.longitude), (latitude, longitude)).miles
        distance_score = 1 / (1 + distance)
    else:
        distance_score = 0

    return round(0.5 * name_score + 0.5 * distance_score, 1)