def make_car(
        manufacturer, model, 
        **car_infos):
    """collect car infos"""
    car_infos['manufacturer'] = manufacturer
    car_infos['model'] = model
    return car_infos
