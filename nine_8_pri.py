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
        

class Privileges:
    """privileges class"""
    def __init__(self, first_name, last_name):
        """initialize"""
        self.privileges = ['add post', 'add users', 'change settings', 
                           'reboot system', '...']
        self.fir_name = first_name
        self.las_name = last_name
            
    def show_privileges(self):
        """display the privileges"""
        print(
            f'{self.fir_name.title()} {self.las_name.title()} has administrator privileges, '
            f'such as:')
        for privilege in self.privileges:
            print(f'- {privilege}')


class Admin(User):
    """administrator users"""
    def __init__(self, first_name, last_name, sex, age, education):
        super().__init__(first_name, last_name, sex, age, education)
        self.admin_privileges = Privileges(first_name, last_name)


autumn = Admin('autumn', 'pai', 'male', 48, 'associate')

autumn.describe_user()
autumn.greet_user()
autumn.admin_privileges.show_privileges()
