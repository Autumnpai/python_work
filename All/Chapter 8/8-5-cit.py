def describe_city(city, country='the USA'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('new york')
describe_city('los angeles')
describe_city('Shenzhen', 'china')
