available_foods = ['banana','cookie', 'ice cream', 'hotdog']
orders = {}

print("List of available foods")
for foods in available_foods:
    print(f"-{foods}")

order_status = True

while order_status:
    name = input("\nWhat's your name? ")
    food = input("What food you want to order? ")
    
    if str(food) not in available_foods:
        print(f"{food.title()} is not available, order again.")
        while food not in available_foods:
            food = input("What food you want to order? ")      


    orders[name] = food
                    
    repeat = input("\nWould you like to order? type yes or no: ")
    if 'no' == repeat.lower():
        order_status = False
            
print("\nList of orders.")
for name, food in orders.items():
    print(f"{name.title()} ordered {food}.")
