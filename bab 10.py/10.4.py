from pathlib import Path

name = input("Please enter your name: ").strip()

path = Path(__file__).parent / 'guest.txt'
path.write_text(name, encoding='utf-8')

print(f"Thanks, {name}! Your name was saved to {path.name}.")