class User:
    """Represent User"""
    def __init__(self, first_name, last_name, age, location):
        """Initializing name"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        """Display the information of the user"""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello, I'm {full_name} and I'm {self.age} years old and I'm from {self.location}.")
        
    def greet_user(self):
        """Greeting the user"""
        print(f"Hello, {self.first_name}! How's your day?")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
                
user1 = User("Lee Adonis", "Lucero", 23, "Tagudin")
user1.describe_user()
user1.greet_user()
print("\n")

user2 = User("Kaye", "Lucero", 25, "Tagudin")
user2.describe_user()
user2.greet_user()
print("\n")

user3 = User("Gors", "Lucero", 2, "Tagudin")
user3.describe_user()
user3.greet_user()

print("\n")

user1.increment_login_attempts()    
user1.increment_login_attempts()   
user1.increment_login_attempts()   

print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
