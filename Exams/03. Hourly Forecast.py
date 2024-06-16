def forecast(*args):
    list_city = {}
    for city, weather in args:
        if city not in list_city:
            list_city[city] = weather
    sorted_result = dict(sorted(list_city.items(), key=lambda x: x[0]))

    sunny = ''
    rainy = ''
    cloudy = ''
    for city, weather in sorted_result.items():
        if weather == 'Sunny':
            sunny += f"{city} - {weather}\n"
        elif weather == 'Rainy':
            rainy += f"{city} - {weather}\n"
        elif weather == 'Cloudy':
            cloudy += f"{city} - {weather}\n"

    return sunny + cloudy + rainy