pets = [
    {
        'owner' : 'gors',
        'kind': 'dog',
    },
    {
        'owner' : 'ilong',
        'kind' : 'cat',
    },
    {
        'owner': 'angel',
        'kind' : 'rabbit',
    }
]
print("Everyone has a pet.")
for pet in pets:
    owner = pet['owner']
    kind = pet['kind'] 
    print(f"\t{owner.title()} loves {kind}.")
        

