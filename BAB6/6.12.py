# Extension of rivers.py: each river now stores its country and its
# approximate length, and the output is formatted as a small table.
rivers = {
    'nile': {'country': 'egypt', 'length_km': 6650},
    'amazon': {'country': 'brazil', 'length_km': 6400},
    'yangtze': {'country': 'china', 'length_km': 6300},
}
 
for river, info in rivers.items():
    country = info['country'].title()
    length = info['length_km']
    print(f"The {river.title()} runs through {country}.")
    print(f"  It is about {length:,} km long.\n")
 
print(f"{'River':<10}{'Country':<10}{'Length (km)':>12}")
for river, info in rivers.items():
    print(
        f"{river.title():<10}{info['country'].title():<10}"
        f"{info['length_km']:>12,}"
    )
 
longest_river = ''
longest_length = 0
for river, info in rivers.items():
    if info['length_km'] > longest_length:
        longest_river = river
        longest_length = info['length_km']
 
print(f"\nThe longest river listed is the {longest_river.title()}.")
 