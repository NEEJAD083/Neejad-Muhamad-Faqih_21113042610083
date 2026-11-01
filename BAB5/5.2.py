# Exercise 5-2: at least one True and one False for each kind of test.
 
# Equality and inequality with strings.
pet = 'dog'
 
print("\nIs pet == 'dog'? I predict True.")
print(pet == 'dog')
 
print("\nIs pet == 'cat'? I predict False.")
print(pet == 'cat')
 
print("\nIs pet != 'cat'? I predict True.")
print(pet != 'cat')
 
print("\nIs pet != 'dog'? I predict False.")
print(pet != 'dog')
 
# Tests using the lower() method.
name = 'Ada Lovelace'
 
print("\nIs name.lower() == 'ada lovelace'? I predict True.")
print(name.lower() == 'ada lovelace')
 
print("\nIs name.lower() == 'Ada Lovelace'? I predict False.")
print(name.lower() == 'Ada Lovelace')
 
# Numerical tests.
age = 21
 
print("\nIs age == 21? I predict True.")
print(age == 21)
 
print("\nIs age == 22? I predict False.")
print(age == 22)
 
print("\nIs age != 22? I predict True.")
print(age != 22)
 
print("\nIs age != 21? I predict False.")
print(age != 21)
 
print("\nIs age > 18? I predict True.")
print(age > 18)
 
print("\nIs age > 21? I predict False.")
print(age > 21)
 
print("\nIs age < 25? I predict True.")
print(age < 25)
 
print("\nIs age < 21? I predict False.")
print(age < 21)
 
print("\nIs age >= 21? I predict True.")
print(age >= 21)
 
print("\nIs age >= 22? I predict False.")
print(age >= 22)
 
print("\nIs age <= 21? I predict True.")
print(age <= 21)
 
print("\nIs age <= 20? I predict False.")
print(age <= 20)
 
# Tests using the and keyword and the or keyword.
print("\nIs age >= 18 and age <= 30? I predict True.")
print(age >= 18 and age <= 30)
 
print("\nIs age >= 18 and age <= 20? I predict False.")
print(age >= 18 and age <= 20)
 
print("\nIs age < 18 or age >= 21? I predict True.")
print(age < 18 or age >= 21)
 
print("\nIs age < 18 or age > 30? I predict False.")
print(age < 18 or age > 30)
 
# Testing whether an item is in a list, and whether it is not.
toppings = ['mushrooms', 'onions', 'pineapple']
 
print("\nIs 'onions' in toppings? I predict True.")
print('onions' in toppings)
 
print("\nIs 'pepperoni' in toppings? I predict False.")
print('pepperoni' in toppings)
 
print("\nIs 'pepperoni' not in toppings? I predict True.")
print('pepperoni' not in toppings)
 
print("\nIs 'onions' not in toppings? I predict False.")
print('onions' not in toppings)
 