guest_list = ['louie', 'mark jay', 'jhun rey', 'angelo']
print("List of attendee")
print(guest_list)
print(f"Good morning {guest_list[0].title()}, you are invited to our dinner.")
print(f"Good morning {guest_list[1].title()}, you are invited to our dinner.")
print(f"Good morning {guest_list[2].title()}, you are invited to our dinner.")
print(f"Good morning {guest_list[3].title()}, you are invited to our dinner.")

print("------------------------------------------------------------------------------------------------------------")

cant_attend = 'angelo'
guest_list.remove(cant_attend)
print(guest_list)
print(f"The person who can't attend is {cant_attend.title()}.")

print("------------------------------------------------------------------------------------------------------------")

print("New list of attendee")

guest_list.insert(1,'patrick')
print(guest_list)
print(f"Good morning {guest_list[0].title()}, you are invited to our dinner.")
print(f"Good morning {guest_list[1].title()}, you are invited to our dinner.")
print(f"Good morning {guest_list[2].title()}, you are invited to our dinner.")
print(f"Good morning {guest_list[3].title()}, you are invited to our dinner.")

print("------------------------------------------------------------------------------------------------------------")

print("Just found a bigger table.")
print("New list of attendee")
guest_list.insert(0, 'robin')
guest_list.insert(2, 'jimrex')
guest_list.append('lander')

print(guest_list)
print(f"Good morning {guest_list[0].title()}, you are invited to our dinner.")
print(f"Good morning {guest_list[1].title()}, you are invited to our dinner.")
print(f"Good morning {guest_list[2].title()}, you are invited to our dinner.")
print(f"Good morning {guest_list[3].title()}, you are invited to our dinner.")
print(f"Good morning {guest_list[4].title()}, you are invited to our dinner.")
print(f"Good morning {guest_list[5].title()}, you are invited to our dinner.")
print(f"Good morning {guest_list[6].title()}, you are invited to our dinner.")

print("------------------------------------------------------------------------------------------------------------")

print("Sorry for the inconvinience, the table wont be arrive on time, we will only have a table for 2 guests.")
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
print("New list of attendee")
print(guest_list)
print(f"Good morning {guest_list[0].title()}, you are invited to our dinner.")
print(f"Good morning {guest_list[1].title()}, you are invited to our dinner.")

print("------------------------------------------------------------------------------------------------------------")

del guest_list[0]
del guest_list[0]
print("Dinner is closed")
print(guest_list)

