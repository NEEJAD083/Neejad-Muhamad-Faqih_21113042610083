import json
from pathlib import Path

path = Path(__file__).parent / 'favorite_number_remembered.json'

if path.exists():
    number = json.loads(path.read_text(encoding='utf-8'))
    print(f"I know your favorite number! It's {number}.")
else:
    while True:
        answer = input("What is your favorite number? ")
        try:
            number = int(answer)
        except ValueError:
            print("Please enter a whole number.")
        else:
            break
    path.write_text(json.dumps(number), encoding='utf-8')
    print("Thanks, I'll remember your favorite number.")