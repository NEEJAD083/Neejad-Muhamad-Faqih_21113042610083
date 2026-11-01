favorite_numbers = {
    'neejad': [3, 53],
    'fatan': [100],
    'repan': [33, 67],
    'nabel': [69],
    'nabil': [1, 2, 3, 4, 5],
}
 
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"  {number}")
    print()
 