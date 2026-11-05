from pathlib import Path

path = Path(__file__).parent / 'learning_python.txt'

# Cara 1: baca seluruh isi file sekaligus
print("Membaca seluruh file sekaligus:")
contents = path.read_text(encoding='utf-8')
print(contents.rstrip())

# Cara 2: simpan baris dalam list, lalu loop satu per satu
print("\nMembaca baris demi baris:")
lines = contents.splitlines()
for line in lines:
    print(line)