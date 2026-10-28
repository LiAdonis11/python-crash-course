def make_car(manufacturer, model_name, **car_details):
    car_details['manufacturer'] = manufacturer
    car_details['model_name'] = model_name
    return car_details
    
car_info = make_car('lamborghini', 'revuelto', color='white and black', feature='aggressive styling')

print(car_info)