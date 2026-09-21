# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Where out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}")

# print("\nFinished making your pizza!")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms','extra cheese','french fries']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else: print(f"Sorry, we dont have {requested_topping}")

print("\nFinished making your pizza!")