cities = {
    'london' : {
        'country' : 'united kingdom',
        'population' : 9.8,
        'fact' : "Home to the world's oldest underground railway network, opened in 1863.",
        },
    'paris' : {
        'country' : 'france',
        'population' : 2.04,
        'fact' : 'Its "City of Light" nickname originally honored its 18th-century philosophers and scientists, not electricity.',
        },
    'tokyo' : {
        'country' : 'japan',
        'population' : 14.27,
        'fact' : ['Stands as the most populous metropolitan area on Earth.', "It features the world's highest density of vending machines, selling everything from hot canned coffee to fresh fruit and umbrellas."],
        },
}

for city, details in cities.items():  
    print(f"City of {city.title()}.")
    print(f"\tCountry: {details['country'].title()}")
    print(f"\tPopulation: approximately {details['population']} million people")
    if isinstance(details['fact'],list):
        for fact in details['fact'] :  
            print(f"\tFact: {fact}")
    else:      
        print(f"\tFact: {details['fact']}")