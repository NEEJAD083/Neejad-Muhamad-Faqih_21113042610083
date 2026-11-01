person_1 = {
    'first_name': 'chandra',
    'last_name': 'wijaya',
    'age': 19,
    'city': 'Bandung',
}
 
person_2 = {
    'first_name': 'stephen',
    'last_name': 'neejad',
    'age': 18,
    'city': 'tangerang',
}
 
person_3 = {
    'first_name': 'adipati',
    'last_name': 'sultan',
    'age': 67,
    'city': 'serang',
}
 
people = [person_1, person_2, person_3]
 
for person in people:
    for key, value in person.items():
        label = key.replace('_', ' ').title()
        print(f"{label}: {value}")
    print()
 