motorcycles = ['honda','yamaha', 'suzuki']
print(motorcycles)
print("------------------------------------------------")

motorcycles[0] = 'ducati'
print(motorcycles)
print("------------------------------------------------")

motorcycles.append('honda')
print(motorcycles)
print("------------------------------------------------")

cars = []

cars.append('honda civic')
cars.append('BMW')
cars.append('audi')
cars.append('tesla')

print(cars)
print("------------------------------------------------")

cars.insert(1,'ford')
print(cars)
print("------------------------------------------------")

del cars[4]
print(cars)
print("------------------------------------------------")

popped_cars = cars.pop()
print(cars)
print(popped_cars)
print("------------------------------------------------")

print(cars)
last_added = cars.pop()
print(f"Last added car was a {last_added.upper()}.")
print(cars)
print("------------------------------------------------")

print(cars)
too_expensive = 'ford'
cars.remove(too_expensive)
print(cars)
print(f"A {too_expensive.title()} is too expensive for me.")

("------------------------------------------------")
