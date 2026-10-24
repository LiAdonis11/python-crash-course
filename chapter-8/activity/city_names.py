def city_country(city_name="tagudin", country_name="philippines"):
    name = f"{city_name}, {country_name}"
    return name.title()

names = city_country("tokyo", "japan")
print(names)
names = city_country("Beijing", "china")
print(names)
names = city_country("los angeles", "united states")
print(names)

    