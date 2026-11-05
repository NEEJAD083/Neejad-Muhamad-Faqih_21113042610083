from pathlib import Path

path = Path(__file__).parent / 'learning_python.txt'
contents = path.read_text(encoding='utf-8')

for line in contents.splitlines():
    print(line.replace('Python', 'C'))