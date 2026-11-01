cities = {
    'tokyo': {
        'country': 'japan',
        'population': 14_000_000,
        'fact': 'It is one of the largest metropolitan areas in the world.',
    },
    'jakarta': {
        'country': 'indonesia',
        'population': 10_500_000,
        'fact': 'It sits on the northwest coast of the island of Java.',
    },
    'cairo': {
        'country': 'egypt',
        'population': 10_000_000,
        'fact': 'The Pyramids of Giza are just outside the city.',
    },
}
 
for city, info in cities.items():
    print(f"{city.title()}:")
    print(f"  Country: {info['country'].title()}")
    print(f"  Population (approximate): {info['population']:,}")
    print(f"  Fact: {info['fact']}")
    print()
 