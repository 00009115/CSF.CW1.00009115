# Dictionary
capitals = {
    # "key": value,
    "Canada":  "Ottawa",
    "France": "Paris",
    "Kazakhstan": "Astana",
    "Russia": "Moscow"
}

continents = {
    "Canada": "North America",
    "France": "Europe",
    "Kazakhstan": "Asia",
    "Russia": ["Asia", "Europe"]   # Dictionary data type can contain another data type inside.
}

# Dictionaries can be differentiated from lists and tuples by them being not index-based but key-based.
# Dictionaries contain much more complex data, namely keys and values which can be updated.
# As the capital city of Kazakhstan has been renamed, let's update the particular dictionary.
capitals["Kazakhstan"] = "Nur-Sultan"


# Let's create a function to use the data provided in the dictionaries above simultaneously.
print("\nDICTIONARY DATA TYPE")
print("--------------\n")   # just for formatting the output in order to keep it clean


# But zipping the dictionaries directly is not a proper action as it zips only the key names but not the values.
# zip(capitals, countries) would return [('Canada', 'Canada'), ('France', 'France'), ... ] which is not what we want.
# What we can do is to extract the items of dictionaries to lists using items() method.

# A function below is meant for giving an information provided in the dictionaries above.

def country_information():
    global capitals
    global continents

    message = input("Do you want to get information about any country? [Type yes/no]: ").lower().strip()
    # validating the input by lower-casing the letters and shrinking the spaces

    if message == "yes":
        print("Available countries:")

        for number, country in enumerate(capitals, 1):   # looping the enumerated dict to print the keys and values
            print("", str(number) + ")", country)

        checking_country_raw = input("Insert the name of the country: ")
        checking_country = checking_country_raw[0].upper() + checking_country_raw[1:].lower()   # validating the input

        if checking_country in capitals and checking_country in continents:
            for (k1, v1), (k2, v2) in zip(capitals.items(), continents.items()):   # looping the zipped dicts
                if k1 == checking_country:
                    if isinstance(v2, str):   # if only 1 continent
                        print("\n", k1, "is situated in", v2, "and its capital city is", v1 + ".")
                    elif isinstance(v2, list):   # if two continents
                        print("\n", k1, "is situated in", v2[0], "and", v2[1] + ". Its capital city is", v1 + ".")
                    print("--------------\n")   # just for formatting the output in order to keep it clean
        else:
            print("\n!!! Please, choose an available country!\n")
        country_information()
    elif message == "no":
        print("--------------\n")   # just for formatting the output in order to keep it clean
        print(" Thank you for using this app! Good bye!")
        return
    else:
        print("\n!!! Please, answer properly!\n")
        country_information()


country_information()   # calling the function to get information about a country
