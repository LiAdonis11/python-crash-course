cars = ['BMW', 'Audi', 'Toyota', 'Ferarri']

if cars[0] == 'BMW':
    print("True")
print("----------------------------------")
if cars[0] != 'bmw':
    print("False") 
print("----------------------------------")
print(len(cars))
print("----------------------------------")
if cars[1].lower() == 'audi':
    print('Lower') 
else:
    print('Capital')
print("----------------------------------")

cars.append('mustang')

if len(cars) == 4:
    print("Equality")
elif len(cars) != 4:
    print("Inequality")

print("----------------------------------")

x = 12
y = 11

if y > x:
    print(f"{y}: is greater than {x}")
elif y >= x:
    print(f"{y} is greater than or equal to {x}")
elif y < x:
    print(f"{y} is less than {x}")
elif y <= x:
    print(f"{y} is less than or equal to {x}")
print("----------------------------------")
    
if x > y and x >= y:
    print("test is correct")

if x > y or x <= y:
    print("Test is correct")
    
print("----------------------------------")

if "Audi" in cars:
    print("Item is in the list")
print("----------------------------------")
if "ebike" in cars:
    print("cars is in the list")
else:
    print("not in the list")
print("----------------------------------")