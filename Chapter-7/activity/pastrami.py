sandwich_orders = ['pastrami','Bánh Mì', 'Croque Monsieur','pastrami', 'Katsu Sando', 'Arepa','pastrami', ]
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")
# if 'pastrami' not in sandwich_orders:
print("Deli has run out of pastrami")
    

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order}")
    finished_sandwiches.append(order)


print("\nList of finished sandwiches")
for orders in finished_sandwiches:
    print(orders)
# print(f"\n{sandwich_orders}")