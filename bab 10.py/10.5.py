from pathlib import Path

names = []

print("Welcome to the guest book. Enter 'q' when you are finished.")
while True:
    name = input("Please enter your name: ").strip()
    if name.lower() == 'q':
        break
    if name:
        names.append(name)
        print(f"Hello, {name}!")

path = Path(__file__).parent / 'guest_book.txt'
if names:
    # Satu nama per baris
    path.write_text("\n".join(names) + "\n", encoding='utf-8')
    print(f"\n{len(names)} name(s) saved to {path.name}.")
else:
    print("\nNo names were entered, so nothing was saved.")