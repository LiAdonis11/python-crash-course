my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
print("My favorite foods are:")
print(my_foods)
print("-----------------------------------------------")
for food in my_foods:
    print(food)

friend_foods.append("ice cream")
print("\nMy friend's favorite foods are:")
print(friend_foods)
print("-----------------------------------------------")
for food in friend_foods:
    print(food)