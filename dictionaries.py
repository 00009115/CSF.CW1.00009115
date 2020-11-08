# Dictionary
capitals = {
    "Canada": {
        "capital": "Ottawa",
    },
    "France": {
        "capital": "Paris",
    },
    "Kazakhstan": {
        "capital": "Astana",
    }
}

continents = {
    "Canada": {
        "continent": "North America"
    },
    "France": {
        "continent": "Europe"
    },
    "Kazakhstan": {
        "continent": "Asia"
    }
}


# Dictionaries contain much more complex data, namely keys and values which can be updated.
# E.g. countries can have more specific information which have been showed using a dictionary above.

# ALl data types can contain another data type which is shown in the dictionaries above. Each values can be edited.
capitals["Kazakhstan"]["capital"] = "Nur-Sultan"

# Zipping the dictionaries directly is not a proper action as it zips only the key names but not the values.
# Therefore we need to extract the items of dictionaries to lists using items() method.
capital_items = capitals.items()
continent_items = continents.items()

# Now we can use zip() function to merge these two lists.
countries = list(zip(capital_items, continent_items))

print("\nZipping:")

for country in countries:
    country_name = country[0][0]
    continent = country[1][1].get("continent")
    capital = country[0][1].get("capital")
    print(country_name, "is located in", continent + ". Its capital is", capital + ".")


# Enumerating the dictionaries directly are not the best solution, because it keeps and numerates only the keys.
# To enumerate the dictionaries items keeping the value as well, we should separate the items out of the dictionary.
ordered_countries = list(enumerate(capitals.items(), 1))  # Second parameter sets the starting point of enumerating.

print("\nEnumerating:")

for country in ordered_countries:
    country_name = country[1][0]
    capital = country[1][1].get("capital")
    print(str(country[0]) + ")", country_name, "-", capital)

