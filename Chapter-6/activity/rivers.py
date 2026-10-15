rivers = {
    'amazon river': 'south america',
    'rio grande': 'north america',
    'rhine river': 'europe'
}

for river in rivers.keys():
    if 'amazon river' in river:
        print("Amazon River: The largest river in the world by water volume, flowing primarily through Brazil, Peru, and Colombia.")
    elif 'rio grande' in river:
        print("Rio Grande: A major border river forming part of the boundary between the United States and Mexico.")
    elif 'rhine river' in river:
        print("Rhine River: A major Western European river flowing through Switzerland, Germany, and the Netherlands.")
    elif 'volga river' in river:
        print("Volga River: The longest river in Europe, flowing entirely through Russia.")
for river, country in rivers.items():
    print(f"{river.title()} : {country.title()}")