country_river = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for river, country in country_river.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in country_river.keys():
    print(river.title())

for country in country_river.values():
    print(country.title())