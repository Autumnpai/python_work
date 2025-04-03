import pytest
from eleven_3 import Employee

@pytest.fixture
def the_employee():
    '''an employee who will be available to all raise functions'''
    autumn = Employee('autumn', 'pai', 240_000)
    return autumn

def test_give_default_raise(the_employee):
    '''test give default raise 5000'''
    the_employee.give_raise()
    assert the_employee.salary == 245000

def test_give_custom_raise(the_employee):
    '''test give custom raise'''
    the_employee.give_raise(50_000)
    assert the_employee.salary == 290_000