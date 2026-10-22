def greet_user(username):
    """Display a simple greeting."""
    print(f"\nHello!, {username.title()}.")

while True:
    print("\nType no if you want to end the program")
    name = input("Whats your name? ")
    
    if name != 'no':
        greet_user(name)
    else:
        break