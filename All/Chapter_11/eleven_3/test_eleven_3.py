from eleven_3 import Employee

def test_give_default_raise():
    '''test give default raise 5000'''
    autumn = Employee('autumn', 'pai', 240_000)
    autumn.give_raise()
    assert autumn.salary == 245000

def test_give_custom_raise():
    '''test give custom raise'''
    autumn = Employee('autumn', 'pai', 240_000)
    autumn.give_raise(50_000)
    assert autumn.salary == 290000