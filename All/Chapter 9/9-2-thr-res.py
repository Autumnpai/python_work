class Restaurant:
    """make a restaurant class"""
    def __init__(self, restaurant_name, cuisine_type):
        """initialize restaurant name and cuisine type"""
        self.res_name = restaurant_name.title()
        self.cui_type = cuisine_type

    def describe_restaurant(self):
        """print the infos"""
        print(f'\nThe name of the restaurant is {self.res_name}.')
        print(f'The cuisine of the restaurant is {self.cui_type}.')

    def open_restanrant(self):
        """tell the restaurant is open"""
        print(f'\nThe {self.res_name} restaurant is open!')


restaurant = Restaurant('jollybee', 'American')
print(restaurant.res_name, f'\n{restaurant.cui_type}')
restaurant.describe_restaurant()
restaurant.open_restanrant()

restaurant1 = Restaurant('luweiju', 'Shandong')
restaurant2 = Restaurant('Saliya', 'Italian')
restaurant3 = Restaurant('lanzhoulamian', 'noodle')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
