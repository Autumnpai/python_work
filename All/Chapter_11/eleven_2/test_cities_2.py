from city_functions import city_functions

def test_city_country_population():
    """test the city country string function"""
    formated_string = city_functions('la', 'usa', 60000000000)
    assert formated_string == 'La, Usa - population 60000000000'