people = [
    {
        'first_name' : 'kaye',
        'last_name' : 'dispo',
        'age' : 25,
        'city' : 'tagudin',
    },
    {
        'first_name' : 'lee',
        'last_name' : 'lucero',
        'age' : 23,
        'city' : 'vigan', 
    },
    {
        'first_name' : 'gors',
        'last_name' : 'lucero',
        'age' : 1,
        'city' : 'tagudin',
    },
]

# print(person['first_name'])
# print(person['last_name'])
# print(person['age'])
# print(person['city'])

for person in people:
    # fullname = f"{person['first_name']} {person['last_name']}"
    if person['age'] == 1:
        print(f"My name is {person['first_name'].title()} {person['last_name'].title()} I'm {person['age']} year old and im from {person['city']}. ")
    else:
        print(f"My name is {person['first_name'].title()} {person['last_name'].title()} I'm {person['age']} years old and im from {person['city']}. ")