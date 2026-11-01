pets = [
    {'name': 'silpa', 'kind': 'beruk', 'owner': 'ghani'},
    {'name': 'silpia', 'kind': 'dog', 'owner': 'neejad'},
    {'name': 'eve', 'kind': 'cow', 'owner': 'padli'},
    {'name': 'Kiwi', 'kind': 'parrot', 'owner': 'Budi'},
]
 
for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value}")
    print()
 