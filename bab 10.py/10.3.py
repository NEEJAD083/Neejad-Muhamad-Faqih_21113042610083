from pathlib import Path

path = Path(__file__).parent / 'pi_digits.txt'
contents = path.read_text(encoding='utf-8')

# file_reader.py (versi ringkas)
print("file_reader:")
for line in contents.splitlines():
    print(line)

# pi_string.py (versi ringkas)
pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print("\npi_string:")
print(pi_string)
print(len(pi_string))