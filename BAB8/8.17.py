"""A module containing one function for making pizza."""
 
 
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
 
# Approach 1: import the whole module
make_pizza(16, 'pepperoni')
 
# Approach 2: import a specific function
make_pizza(12, 'mushrooms', 'green peppers')
 
# Approach 3: import a function with an alias
make_pizza(9, 'extra cheese')
 
# Approach 4: import a module with an alias
make_pizza(14, 'bacon', 'pineapple')
 
# Approach 5: import all functions from a module
make_pizza(10, 'spinach')
 