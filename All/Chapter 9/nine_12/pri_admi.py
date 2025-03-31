from user import User

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