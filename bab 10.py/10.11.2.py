import json
from pathlib import Path

path = Path(__file__).parent / 'favorite_number.json'

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print("I don't know your favorite number yet. Run the writer program first.")
else:
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")