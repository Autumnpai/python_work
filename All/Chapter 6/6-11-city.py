cities = {}
los_angeles = {
    'country': 'United States',
    'population': 3976000,
    'fact': 'The city is known for its Mediterranean climate',
    }

binzhou = {
    'country': 'China',
    'population': 3450000,
    'fact': 'The city is known for its Yellow River Delta',
    }

beijing = {
    'country': 'China',
    'population': 21540000,
    'fact': 'The city is known for its Forbidden City',
    }

cities['Los Angeles'] = los_angeles
cities['Binzhou'] = binzhou
cities['Beijing'] = beijing

for city, city_info in cities.items():
    print(
        f"\n{city} is in {city_info['country']}. "
        f"It has a population of {city_info['population']}. "
        f"{city_info['fact']}."
        )