# Creating an empty dictionary -  that is where we store our key value pairs
vacation = {}

# Setting the program to continue loop
poll = True

# Creating the loop
while poll:
    name = input("\nWhat's your name? ")
    destination = input("One place you want to visit? ")
    
    # Assign the input values to the dictionary
    vacation[name] = destination
    
    repeat = input("\nWould you like to create another poll? yes/no ")
    if 'no' == repeat.lower():
        poll = False
            
print("\nPoll results")
for name, destination in vacation.items():
    print(f"Hi {name.title()}, your dream vacation is {destination.title()}")


