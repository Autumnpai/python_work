from pathlib import Path
import json

path = Path('fav_num.json')

read_contents = path.read_text()
contents = json.loads(read_contents)
print(f'I know your favorite number! it is {contents}')
