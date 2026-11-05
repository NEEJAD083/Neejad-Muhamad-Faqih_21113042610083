import json
from pathlib import Path

while True:
    answer = input("What is your favorite number? ")
    try:
        number = int(answer)
    except ValueError:
        print("Please enter a whole number.")
    else:
        break

path = Path(__file__).parent / 'favorite_number.json'
path.write_text(json.dumps(number), encoding='utf-8')
print("Thanks, your favorite number has been saved.")