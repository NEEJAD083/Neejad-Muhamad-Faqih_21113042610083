from pathlib import Path

texts_dir = Path(__file__).parent / 'texts'
paths = sorted(texts_dir.glob('*.txt'))

if not paths:
    print("No .txt files found in the 'texts' folder.")

for path in paths:
    try:
        contents = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        print(f"\n{path.name}: could not be read as UTF-8 text, skipping.")
        continue

    lowered = contents.lower()
    count_the = lowered.count('the')
    count_the_space = lowered.count('the ')

    print(f"\n{path.name}:")
    print(f"  'the'  appears about {count_the} times")
    print(f"  'the ' appears about {count_the_space} times")