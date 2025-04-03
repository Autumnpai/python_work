def city_functions(city, country, population=""):
    """format city coutry strings"""
    if population:
        string = f"{city.title()}, {country.title()} - population {population}"
    else:
        string = f"{city.title()}, {country.title()}"
    return string

# print(city_functions('la', 'usa', 6_000_000))