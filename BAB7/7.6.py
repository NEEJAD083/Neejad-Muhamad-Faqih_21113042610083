prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "
 
# Version 1: a conditional test in the while statement stops the loop.
print("Version 1: conditional test")
topping = input(prompt)
while topping != 'quit':
    print(f"I'll add {topping} to your pizza.")
    topping = input(prompt)
 
# Version 2: an active variable controls how long the loop runs.
print("\nVersion 2: active variable")
active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")
 
# Version 3: a break statement exits the loop.
print("\nVersion 3: break statement")
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")
 