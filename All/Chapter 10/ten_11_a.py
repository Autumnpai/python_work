from pathlib import Path
import json

path = Path('fav_num.json')
fav_num = input('What is your favorate number? ')
contents_json = json.dumps(fav_num)
path.write_text(contents_json)
