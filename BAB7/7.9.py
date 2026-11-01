sandwich_orders = [
    'pastrami', 'tuna', 'pastrami', 'turkey', 'veggie', 'pastrami', 'ham',
]
finished_sandwiches = []
 
print("Sorry, the deli has run out of pastrami.")
 
# Remove every pastrami sandwich from the orders.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
 
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
 
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"  {sandwich.title()}")
 