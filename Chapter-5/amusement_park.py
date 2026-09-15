age = 102

# if age < 4:
#     print("Admission for anyone under age 4 is free")
# elif age < 18:
#     print("Admission for anyone between the ages 4 abd 18 is 25$")
# else:
#     print("Admission for anyone age 18 or older is 40$")


if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your adimission cost is {price}$.")