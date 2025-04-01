from pathlib import Path

file_names = ['dogs.txt', 'cats.txt']

for name in file_names:
    try:
        print(Path(name).read_text())
    except FileNotFoundError:
        pass