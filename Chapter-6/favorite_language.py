favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# for name, language in favorite_language.items():
#     print(f"{name.title()}'s favorite language is {language.title()}. ")

# print("-------------------------------------------------------------")

# language = favorite_language['sarah'].title()
# print(f"Sarah's favorite language is {language}.")


# for name in favorite_language.keys():
#     print(name.title())
people = ['jen','phil','may']
for name in favorite_language.keys():
    
    if name in people:
        print(f"Thank you for taking the poll {name}.")
if 'may' not in favorite_language.keys():
    print(f"Please take the poll may")