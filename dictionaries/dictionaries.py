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

# Dictionaries are differentiated from lists and tuples because they are not index-based but key-based.
# Dictionaries contain much more complex data, namely keys and values which can be updated.
capitals["Kazakhstan"] = "Nur-Sultan"


# Let's create a function to use the data provided in the dictionaries above simultaneously.
print("\nDICTIONARY DATA TYPE")
print("--------------\n")   # for formatting, keeping the output in order and clean


# But zipping the dictionaries directly is not a proper action as it zips only the key names but not the values.
# zip(capitals, countries) would return [('Canada', 'Canada'), ('France', 'France'), ... ] which is not good.
# What we can do is to extract the items of dictionaries to lists using items() method.

def country_information():
    global capitals
    global continents

    message = input("Do you want to get information about any country? [Type yes/no]: ").lower().strip()
    # validating the input by lower-casing the letters and shrinking the spaces

    if message == "yes":
        print("Available countries:")

        for number, country in enumerate(capitals, 1):
            print("", str(number) + ")", country)

        checking_country_raw = input("Insert the name of the country: ")
        checking_country = checking_country_raw[0].upper() + checking_country_raw[1:].lower()   # validating the input

        if checking_country in capitals:
            for (k1, v1), (k2, v2) in zip(capitals.items(), continents.items()):
                if k1 == checking_country:
                    if isinstance(v2, str):
                        print("\n", k1, "is situated in", v2, "and its capital city is", v1 + ".")
                    elif isinstance(v2, list):
                        print("\n", k1, "is situated in", v2[0], "and", v2[1] + ". Its capital city is", v1 + ".")
                    print("--------------\n")  # for formatting, keeping the output in order and clean
        else:
            print("\n!!! Please, choose an available country!\n")
        country_information()
    elif message == "no":
        print("--------------\n")  # for formatting, keeping the output in order and clean
        print(" Thank you for using this app! Good bye!")
        return
    else:
        print("\n!!! Please, answer properly!\n")
        country_information()


country_information()  # calling the function to get information about a country

#
# capital_items = capitals.items()
# continent_items = continents.items()
#
# # Still zipping this two data is not a proper option. zip(capital_items, continent_items) returns the list below:
# # [(('Canada', 'Ottawa'), ('Canada', 'North America')), (('France', 'Paris'), ('France', 'Europe')), ... ))].
#
# # We can get much more comprehensive dictionary by looping this list.
#
# countries = dict()
#
# for (country, capital), (c, continent) in zip(capital_items, continent_items):
#     countries[country] = dict(capital=capitals[country], continent=continents[country])
#
# # Now countries is a dictionary received out of merging capitals and continents dictionaries comprehensively.
# # countries = {'Canada': {'capital': 'Ottawa', 'continent': 'North America'}, ... }
#
# # Using the data we reproduced above:
# print("\nZipping:")
#
# for country in countries:
#     if country == "Russia":
#         print(country, "is located in", countries[country]["continent"][0], "and", countries[country]["continent"][1],
#               "and its capital is", countries[country]["capital"])
#     else:
#         print(country, "is located in", countries[country]["continent"],
#               "and its capital is", countries[country]["capital"])
#
# # ENUMERATING
#
# # Enumerating the dictionaries directly are not the best solution, because it keeps and numerates only the keys.
# # enumerate(countries) returns [(0, 'Canada'), (1, 'France'), (2, 'Kazakhstan'), (3, 'Russia')]
# # To keep the values while enumerating, we can extract the items out of the dictionary into the list.
# numbered_countries = list(enumerate(countries.items(), 1))  # Second parameter sets the starting point of enumerating.
#
# # Using the data we reproduced above
# print("\nEnumerating:")
#
# for country in numbered_countries:   # = (1, ('Canada', {'capital': 'Ottawa', 'continent': 'North America'})) etc.
#     country_info = country[1]        # = ('Canada', {'capital': 'Ottawa', 'continent': 'North America'}) etc.
#     country_name = country_info[0]   # = 'Canada' etc.
#     capital = country_info[1]["capital"]      # = 'Ottawa' etc.
#     continent = country_info[1]["continent"]  # = 'North America' etc.
#     if country_name == "Russia":
#         print(str(country[0]) + ")", capital + ",", country_info[0] + ",", continent[0], "/", continent[1])
#     else:
#         print(str(country[0]) + ")", capital + ",", country_info[0] + ",", continent)
