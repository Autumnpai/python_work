import car_fun
from car_fun import make_car
from car_fun import make_car as mc
import car_fun as cf
from car_fun import *

# import car_fun

car = car_fun.make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)

car = car_fun.make_car('tesla', 'model 3', type = 'base', quality = 'great', power = 'very strong')
print(car)
print()

# from car_fun import make_car
car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)

car = make_car('tesla', 'model 3', type = 'base', quality = 'great', power = 'very strong')
print(car)
print()

# from car_fun import make_car as mc

car = mc('subaru', 'outback', color = 'blue', tow_package = True)
print(car)

car = mc('tesla', 'model 3', type = 'base', quality = 'great', power = 'very strong')
print(car)
print()

# import car_fun as cf

car = cf.make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)

car = cf.make_car('tesla', 'model 3', type = 'base', quality = 'great', power = 'very strong')
print(car)
print()

#from car_fun import *

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)

car = make_car('tesla', 'model 3', type = 'base', quality = 'great', power = 'very strong')
print(car)
print()