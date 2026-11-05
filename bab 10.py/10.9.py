from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(__file__).parent / filename
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass  # gagal secara diam-diam
    else:
        print(f"\nContents of {filename}:")
        print(contents.rstrip())