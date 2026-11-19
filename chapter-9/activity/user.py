class User:
    """Represent User"""
    def __init__(self, first_name, last_name, age, location):
        """Initializing name"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    
    def describe_user(self):
        """Display the information of the user"""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello, I'm {full_name} and I'm {self.age} years old and I'm from {self.location}.")
        
    def greet_user(self):
        """Greeting the user"""
        print(f"Hello, {self.first_name}! How's your day?")
        
class Admin(User):
    def __init__(self, first_name, last_name, age, location, privileges):
        super().__init__(first_name, last_name, age, location)
        self.privileges = privileges
    
    def show_privileges(self):
        print("The admin can:")
        for privilege in self.privileges:
            print(f"- {privilege}")
               
        
        
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

admin = Admin('lee', 'lucero', 23, 'tag', ['can add post', 'can delete post', 'can be user'])
admin.describe_user()
admin.greet_user()
admin.show_privileges()
        
        