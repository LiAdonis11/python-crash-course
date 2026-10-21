prompt = ("Enter your age\n")
prompt += ("Enter (0) to submit: ")

while True:
    age = input(prompt)
    age = int(age)
    if age == 0:
        break
    if age < 3:
            print("Your ticket is free.")
    elif age >= 3 and age <= 12:
       print("Your ticket is $10.")
    elif age > 12:
        print("Your ticket is $15.")
        