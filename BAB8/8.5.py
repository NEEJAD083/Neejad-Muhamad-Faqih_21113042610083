def describe_city(city, country='Indonesia'):
    """Display a simple message about a city and the country it is in."""
    print(f"{city.title()} is in {country.title()}.")
 
 
describe_city('jakarta')
describe_city('bandung')
describe_city('reykjavik', 'iceland')
 