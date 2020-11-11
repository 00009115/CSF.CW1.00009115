# Dictionary
capitals = {
    "Canada":  "Ottawa",
    "France": "Paris",
    "Kazakhstan": "Astana",
    "Russia": "Moscow"
}

continents = {
    "Canada": "North America",
    "France": "Europe",
    "Kazakhstan": "Asia",
    "Russia": ["Asia", "Europe"]  # ALl data types can contain another data type inside.
}

# Dictionaries contain much more complex data, namely keys and values which can be updated.
capitals["Kazakhstan"] = "Nur-Sultan"

# ZIPPING

# Zipping the dictionaries directly is not a proper action as it zips only the key names but not the values.
# zip(capitals, countries) would return [('Canada', 'Canada'), ('France', 'France'), ... ] which is not good.

# What we can do is to extract the items of dictionaries to lists using items() method.
capital_items = capitals.items()
continent_items = continents.items()

# Still zipping this two data is not a proper option. zip(capital_items, continent_items) returns the list below:
# [(('Canada', 'Ottawa'), ('Canada', 'North America')), (('France', 'Paris'), ('France', 'Europe')), ... ))].

# We can get much more comprehensive dictionary by looping this list.

countries = dict()

for (country, capital), (c, continent) in zip(capital_items, continent_items):
    countries[country] = dict(capital=capitals[country], continent=continents[country])

# Now countries is a dictionary received out of merging capitals and continents dictionaries comprehensively.
# countries = {'Canada': {'capital': 'Ottawa', 'continent': 'North America'}, ... }

# Using the data we reproduced above:
print("\nZipping:")

for country in countries:
    if country == "Russia":
        print(country, "is located in", countries[country]["continent"][0], "and", countries[country]["continent"][1],
              "and its capital is", countries[country]["capital"])
    else:
        print(country, "is located in", countries[country]["continent"],
              "and its capital is", countries[country]["capital"])

# ENUMERATING

# Enumerating the dictionaries directly are not the best solution, because it keeps and numerates only the keys.
# enumerate(countries) returns [(0, 'Canada'), (1, 'France'), (2, 'Kazakhstan'), (3, 'Russia')]
# To keep the values while enumerating, we can extract the items out of the dictionary into the list.
numbered_countries = list(enumerate(countries.items(), 1))  # Second parameter sets the starting point of enumerating.

# Using the data we reproduced above
print("\nEnumerating:")

for country in numbered_countries:   # = (1, ('Canada', {'capital': 'Ottawa', 'continent': 'North America'})) etc.
    country_info = country[1]        # = ('Canada', {'capital': 'Ottawa', 'continent': 'North America'}) etc.
    country_name = country_info[0]   # = 'Canada' etc.
    capital = country_info[1]["capital"]      # = 'Ottawa' etc.
    continent = country_info[1]["continent"]  # = 'North America' etc.
    if country_name == "Russia":
        print(str(country[0]) + ")", capital + ",", country_info[0] + ",", continent[0], "/", continent[1])
    else:
        print(str(country[0]) + ")", capital + ",", country_info[0] + ",", continent)
