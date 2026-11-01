# Exercise 5-1: ten conditional tests (five True, five False).
car = 'subaru'
 
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
 
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
 
print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')
 
print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')
 
print("\nIs car == 'Subaru'? I predict False.")
print(car == 'Subaru')
 
print("\nIs car.title() == 'Subaru'? I predict True.")
print(car.title() == 'Subaru')
 
print("\nIs car.upper() == 'SUBARU'? I predict True.")
print(car.upper() == 'SUBARU')
 
print("\nIs car.upper() == 'subaru'? I predict False.")
print(car.upper() == 'subaru')
 
print("\nIs car == 'subaru ' (with a trailing space)? I predict False.")
print(car == 'subaru ')
 
print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')