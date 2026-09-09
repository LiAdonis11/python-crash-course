pizzas = ['bbq', 'hawaiian', 'pepperoni']

for pizza in pizzas:
    print(f'I like to eat {pizza.title()} pizza.')
print("Its one of my favorite snacks.")

friend_pizzas = pizzas[:]
print(pizzas)
print(friend_pizzas)


pizzas.append('ham and cheese')
friend_pizzas.append('spicy fish')

print("\n")

print(pizzas)
print(friend_pizzas)

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\n")

print("My friends's favorite pizza are:")
for pizza in friend_pizzas:
    print(pizza)
    
