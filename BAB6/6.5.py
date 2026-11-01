rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}
 
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
 
print("\nThe rivers in the dictionary are:")
for river in rivers.keys():
    print(river.title())
 
print("\nThe countries in the dictionary are:")
for country in rivers.values():
    print(country.title())
 