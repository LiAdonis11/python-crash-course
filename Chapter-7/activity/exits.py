prompt = ("Enter your age\n")
prompt += ("Enter (quit) to submit: ")

active = True
while active:
    age = input(prompt)
    if str(age) == 'quit':
        active = False
    else:
        if int(age) < 3:
            print("Your ticket is free.")
        elif int(age) >= 3 and int(age) <= 12:
            print("Your ticket is $10.")
        elif int(age) > 12:
            print("Your ticket is $15.")
        