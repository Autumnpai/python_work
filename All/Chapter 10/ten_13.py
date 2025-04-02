from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    userinfo = {}
    userinfo['username'] = input("What is your name? ").title()
    userinfo['sex'] = input('What is your sex (M/F)? ').title()
    userinfo['email'] = input('What is your email? ')
    userinfo['city'] = input('Which city are you living in? ').title()
    contents = json.dumps(userinfo)
    path.write_text(contents)
    return userinfo

def greet_user():
    """Greet the user by name."""
    path = Path('userinfo.json')
    userinfo = get_stored_username(path)
    if userinfo:
        print(f"Welcome back, {userinfo['username']}!")
        for each_key in userinfo.keys():
            print(f'{each_key}: {userinfo[each_key]}')
    else:
        userinfo = get_new_username(path)
        print(f"We'll remember you when you come back, {userinfo['username']}!")

greet_user()