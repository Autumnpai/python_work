class User:
    def __init__(self, first_name, last_name, sex, age, education):
        """initial the class"""
        self.fir_name = first_name.title()
        self.las_name = last_name.title()
        self.x = sex
        self.edu = education
        self.ag = age
        self.login_attempts = 0
    
    def describe_user(self):
        print(f'\nThe basic infos of the user:')
        print(f'Name: {self.fir_name} {self.las_name}')
        print(f'Sex: {self.x}\nAge: {self.ag}\nEducation: {self.edu}')
    
    def greet_user(self):
        print(f'\nHello {self.fir_name} {self.las_name}!')

    def incrment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

autumn = User('autumn', 'pai', 'male', 48, 'associate')

for each in range(1,24):
    autumn.incrment_login_attempts()
print(
    f'The number {autumn.fir_name} {autumn.las_name} appempted to login is '
    f'{autumn.login_attempts}.')

autumn.reset_login_attempts()
print(
    f'The number {autumn.fir_name} {autumn.las_name} appempted to login is '
    f'reset to {autumn.login_attempts}.')

