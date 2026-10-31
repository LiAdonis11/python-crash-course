class Restaurant:
    """Represent a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Display the restaurant name and cusine type."""
        print(f"The name of the restaurant is {self.restaurant_name} and their cuisine type is {self.cuisine_type}.")
    def open_restaurant(self):
        """Display the restaurant operating status."""
        print(f"The restaurant is open!")

restaurant = Restaurant('Mr.Li', 'Asian')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

