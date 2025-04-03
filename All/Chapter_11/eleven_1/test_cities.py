from eleven_1 import city_functions

def test_city_country():
    """test the city country string function"""
    formated_string = city_functions('la', 'usa')
    assert formated_string == 'La, Usa'