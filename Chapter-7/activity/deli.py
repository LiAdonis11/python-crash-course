sandwich_orders = ['Bánh Mì', 'Croque Monsieur', 'Katsu Sando', '']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order}")
    finished_sandwiches.append(order)


print("\nList of finished sandwiches")
for orders in finished_sandwiches:
    print(orders)
print(f"\n{sandwich_orders}")