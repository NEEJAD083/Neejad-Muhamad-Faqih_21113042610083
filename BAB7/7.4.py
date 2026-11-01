prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "
 
topping = input(prompt)
 
while topping != 'quit':
    print(f"I'll add {topping} to your pizza.")
    topping = input(prompt)
 