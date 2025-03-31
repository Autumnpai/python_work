class User:
    """users"""
    def __init__(self, first_name, last_name, sex, age, education):
        """initial the class"""
        self.fir_name = first_name.title()
        self.las_name = last_name.title()
        self.x = sex
        self.edu = education
        self.ag = age
    
    def describe_user(self):
        print(f'\nThe basic infos of the user:')
        print(f'Name: {self.fir_name} {self.las_name}')
        print(f'Sex: {self.x}\nAge: {self.ag}\nEducation: {self.edu}')
    
    def greet_user(self):
        print(f'\nHello {self.fir_name} {self.las_name}!')