class Restaurant:
    """make a restaurant class"""
    def __init__(self, restaurant_name, cuisine_type):
        """initialize restaurant name and cuisine type"""
        self.res_name = restaurant_name.title()
        self.cui_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """print the infos"""
        print(f'The name of the restaurant is {self.res_name}.')
        print(f'The cuisine of the restaurant is {self.cui_type}.')

    def open_restanrant(self):
        """tell the restaurant is open"""
        print(f'The {self.res_name} restaurant is open!')

    def set_number_served(self, num_served):
        """set the number of the served people"""
        self.number_served = num_served
    
    def increment_number_served(self, num_increment):
        """increment the number"""
        self.number_served += num_increment


restaurant = Restaurant('jollybee', 'American')

# print the number of the served people
print(restaurant.number_served)

# change the number the served people and print
restaurant.number_served = 699999999
print(restaurant.number_served)

# use method to change the number
restaurant.set_number_served(24654799)
print(restaurant.number_served)

# use method to increment the number
restaurant.increment_number_served(8098912)
print(restaurant.number_served)

