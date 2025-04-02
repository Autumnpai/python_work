from pathlib import Path

files_name = ['Hamlet.txt', 'Anne of Green Gables.txt', 
              'the Adventures of Tom Sawyer.txt', 'David Copperfield.txt']

for name in files_name:
    path = Path(name)
    try:
        contents = path.read_text()
        print(
            f'The number of "the" in {path.stem} is approximately: '
            f'{contents.lower().count('the')}')
        print(
            f'The number of "the " in {path.stem} is approximately: '
            f'{contents.lower().count('the ')}')
    except:
        print(f"{path} is not found!")