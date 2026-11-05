from city_functions import get_city_country


def test_city_country():
    formatted = get_city_country('santiago', 'chile')
    assert formatted == 'Santiago, Chile'