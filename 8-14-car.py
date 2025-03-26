def make_car(
        manufacturer, model, 
        **car_infos):
    """collect car infos"""
    car_infos['manufacturer'] = manufacturer
    car_infos['model'] = model
    return car_infos

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)

car = make_car('tesla', 'model 3', type = 'base', quality = 'great', power = 'very strong')
print(car)