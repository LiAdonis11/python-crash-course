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
        'fact' : 'Stands as the most populous metropolitan area on Earth.',
        },
}

for city, details in cities.items():
    print(f"City of {city.title()}.")
    country = details['country']
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: approximately {details['population']} million people")        
    print(f"\tFact: {details['fact']}")