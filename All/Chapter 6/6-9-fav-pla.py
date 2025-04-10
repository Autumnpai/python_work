favorate_places = {}
favorate_places['mickey'] = ['Los Angeles', 'Shenzhen', 'Taipei']
favorate_places['doudou'] = ['Shenzhen', 'Los Angeles', 'Paris']
favorate_places['yali'] = ['Beijing', 'Matis', 'Binzhou']

for person, places in favorate_places.items():
    print(
        f"\n{person.title()}'s favorite places are: "
        f"{places[0]}, {places[1]}, {places[2]}."
        )
    

