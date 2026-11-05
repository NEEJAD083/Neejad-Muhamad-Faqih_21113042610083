print("Addition calculator. Enter 'q' at any prompt to quit.")

while True:
    first = input("\nFirst number: ")
    if first.lower() == 'q':
        break

    second = input("Second number: ")
    if second.lower() == 'q':
        break

    try:
        total = int(first) + int(second)
    except ValueError:
        print("Sorry, that doesn't look like a whole number. Please try again.")
    else:
        print(f"The sum is {total}.")

print("Goodbye!")