from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

# contents_lines = contents.splitlines()
for line in contents.splitlines():
   print(line)
