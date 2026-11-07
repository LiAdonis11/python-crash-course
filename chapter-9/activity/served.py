class Restaurant:
    """Represent a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type 
        self.number_served = 0
        
    def describe_restaurant(self):
        """Display the restaurant name and cusine type."""
        print(f"The name of the restaurant is {self.restaurant_name} and their cuisine type is {self.cuisine_type}.")
        
    def open_restaurant(self):
        """Display the restaurant operating status."""
        print(f"The restaurant is open!")
        
    def set_number_served(self, total):
        self.number_served = total
        print(f"Number of customers served: {self.number_served}")
    
    def increment_number_served(self, additional):  
        self.number_served += additional
        print(f"Updated total number of customer: {self.number_served}")

restaurant = Restaurant('Mr.Li', 'Asian')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"The restuarant served: {restaurant.number_served}")
restaurant.number_served = 10
print(f"The restaurant serve: {restaurant.number_served}\n")

restaurant.set_number_served(56)

restaurant.increment_number_served(33)

