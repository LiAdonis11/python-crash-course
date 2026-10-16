favorite_places = {
    'kaye' : 
        ['tarlac', 'vigan', 'pangasinan'],
    'lee' : 
        ['tagudin', 'vigan', 'tarlac'],
    'gors' : ['pudoc', 'sawat', 'caoayan']
}

for person, place in favorite_places.items():
    print(f"{person.title()}'s favorite places are: ")
    for places in place:
        print(f"\t {places.title()}")