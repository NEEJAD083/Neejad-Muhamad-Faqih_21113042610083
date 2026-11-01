pizzas = ["pepperoni", "margherita", "hawaiian"]
 
# First, just print the name of each pizza.
for pizza in pizzas:
    print(pizza)
 
# Now print a sentence about each pizza.
print()
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
 
# This line is outside the loop, so it prints only once.
print("\nI really love pizza!")