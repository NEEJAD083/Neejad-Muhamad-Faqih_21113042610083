import json
from pathlib import Path


def get_stored_username(path):
    """Ambil nama pengguna yang tersimpan, jika ada."""
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        return json.loads(contents)
    return None


def get_new_username(path):
    """Minta nama pengguna baru dan simpan."""
    username = input("What is your name? ")
    path.write_text(json.dumps(username), encoding='utf-8')
    return username


def greet_user():
    """Sapa pengguna, setelah memastikan namanya benar."""
    path = Path(__file__).parent / 'username.json'
    username = get_stored_username(path)
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct.strip().lower() == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()