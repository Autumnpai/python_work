from pathlib import Path
import json

path = Path('fav_num.json')

if path.exists():
    read_contents = path.read_text()
    contents = json.loads(read_contents)
    print(f'I know your favorite number! it is {contents}')
else:
    fav_num = input('What is your favorate number? ')
    contents_json = json.dumps(fav_num)
    path.write_text(contents_json)