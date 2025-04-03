class Employee:
    """name and salary of an employee"""
    def __init__(self, first_name, last_name, salary):
        """initial"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self, amount=5000):
        '''raise salary'''
        self.salary += amount

'''
autumn = Employee('autumn', 'pai', 240_000)

print(autumn.salary)
autumn.give_raise()
print(autumn.salary)
autumn.give_raise(1000000)
print(autumn.salary)'
'''