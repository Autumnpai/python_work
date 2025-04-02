from pathlib import Path

file_names = ['dogs.txt', 'cats.txt']

for name in file_names:
    try:
        print(Path(name).read_text())
    except FileNotFoundError:
        print(f"Sorry, please make sure {name} in the directory.")