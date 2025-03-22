favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

poll_names = ['autumn','sarah', 'phil',  'hebe']

for name in poll_names:
    if name in favorite_languages.keys():
        print(f'Thank your for taking the poll, {name.title()}!')
    else:
        print(f'What is your favorite language, {name.title()}?')
