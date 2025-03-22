glossary = {
    'list': "a collection of data.",
    'dictionary': 'a collection of data by pairs.',
    'function': 'a command to do something.',
    'integer': 'numbers.',
    'float': 'numbers with decimals.',
    'tuple': 'a collection of data that cannot be changed.',
    'set': 'a collection of data that cannot have duplicates.',
    'string': 'a collection of characters.',
    'boolean': 'a true or false value.',
    'variable': 'a placeholder for data.',
}

for term, meaning in glossary.items():
    print(f"{term.title()}:\n    {meaning.title()}\n")