pets = []
pet1 = {'kind': 'dog', 'owner': 'mickey'}
pet2 = {'kind': 'cat', 'owner': 'doudou'}
pet3 = {'kind': 'fish', 'owner': 'yali'}

pets.append(pet1)
pets.append(pet2)
pets.append(pet3)

for pet in pets:
    print(
        f"\n{pet['owner'].title()}'s pet is a {pet['kind']}."
    )