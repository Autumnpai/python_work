from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

contents_lines = contents.splitlines()
for line in contents_lines:
   print(line.replace('python', 'C').replace('Python', 'C'))