numbers = {
    'kaye' : [28, 3, 1],
    'louie' : [13, 1],
    'mak' : [26],
    'anli' : [],
    'lee' : [11, 4, 3],
}

# print(numbers['lee'])
# print(numbers['kaye'])
# print(numbers['louie'])
# print(numbers['mak'])
# print(numbers['anli'])

for person, number in numbers.items():
    if len(number) > 1:
        print(f"{person.title()}'s favorite numbers are:")
        for num in number:
            print(f"\t{num}")
    elif len(number) == 1:
        print(f"{person.title()}'s favorite number is {number[0]}.")
    else:
        print(f"{person.title()} hasn't picked a number yet.")