favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'ana': 'python',
    'phil': 'python',
}
 
people = ['jen', 'ana', 'phil', 'budi', 'sarah']
 
for person in people:
    if person in favorite_languages:
        print(f"Thank you for responding to the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take our favorite languages poll!")
 