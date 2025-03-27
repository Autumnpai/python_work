people = []
people.append({
    'first_name': 'Quantum',
    'last_name': 'Pai',
    'age': 4,
    'city': "Los Angeles", 
    })
people.append({
    'first_name': 'Dixue',
    'last_name': 'Tang',
    'age': 18,
    'city': 'Binzhou',
    })
people.append({
    'first_name': 'Yali',
    'last_name': 'Tang',
    'age': 31,
    'city': 'Beijing',
    })

for person in people:
    print(
        f"\n{person['first_name']} {person['last_name']} is "
        f"{person['age']} years old, lives in {person['city']}."
    )

