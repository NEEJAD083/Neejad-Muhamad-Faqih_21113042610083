import json
from pathlib import Path


def get_stored_user(path):
    """Ambil dictionary pengguna dari file jika ada."""
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        return json.loads(contents)
    return None


def get_new_user(path):
    """Tanya data pengguna baru, simpan sebagai dictionary ke file."""
    user = {
        'username': input("What is your name? "),
        'hometown': input("Where are you from? "),
        'hobby': input("What is your favorite hobby? "),
    }
    path.write_text(json.dumps(user), encoding='utf-8')
    return user


def show_summary(user):
    """Cetak ringkasan semua yang diingat program."""
    print("\nHere is what I remember about you:")
    print(f"  Name:     {user['username']}")
    print(f"  Hometown: {user['hometown']}")
    print(f"  Hobby:    {user['hobby']}")


def remember_user():
    path = Path(__file__).parent / 'user_profile.json'
    user = get_stored_user(path)
    if user:
        print(f"Welcome back, {user['username']}!")
    else:
        user = get_new_user(path)
        print(f"We'll remember you when you come back, {user['username']}!")
    show_summary(user)


remember_user()