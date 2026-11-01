prompt = "\nHow old are you? "
prompt += "Enter 'quit' when you are finished: "
 
age = input(prompt)
 
while age != 'quit':
    age = int(age)
 
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
 
    age = input(prompt)
 