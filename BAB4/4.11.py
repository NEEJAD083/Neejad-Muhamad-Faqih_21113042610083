pizzas = ["pepperoni", "margherita", "hawaiian"]
 
# Make a separate copy of the list with a slice.
friend_pizzas = pizzas[:]
 
pizzas.append("four cheese")
friend_pizzas.append("bbq chicken")
 
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
 
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
 