class Restaurant:
    """Represent restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Display the restaurant description"""
        print(f"The restaurant name is {self.restaurant_name} and its cuisine type is {self.cuisine_type}.")
        
    def open_restaurant(self):
        """Display restaurant operating status"""
        print(f"The restaurant is open.")

make_restaurant = Restaurant('Mr.Lee', 'Asian')

make_restaurant.describe_restaurant()
make_restaurant.open_restaurant()

print(make_restaurant.restaurant_name)
print(make_restaurant.cuisine_type)
print("\n")

make_restaurant1 = Restaurant('Kayekaye', 'American')
make_restaurant1.describe_restaurant()
make_restaurant2 = Restaurant('Gors', 'Egyptian')
make_restaurant2.describe_restaurant()
make_restaurant3  =Restaurant('LI', 'Asian')
make_restaurant3.describe_restaurant()

    
    