def city_country(city, country):
    """format city and country"""
    formatted = city.title() + ", " + country.title()
    return formatted

print(city_country('santiago', 'chile'))
print(city_country('beijing', 'china'))
print(city_country('tokyo', 'japan'))