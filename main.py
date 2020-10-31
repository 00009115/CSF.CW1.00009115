# List
transports = ["airplane", "train", "car", "bus", "ferry"]

# Lists contain simple data (item) and can be edited afterwards.

# E.g. as transport types are not as limited as in this list, it can be updated by adding or removing.
transports.append("helicopter")

#########

# Tuple
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
weekends = ("Saturday", "Sunday")

# Tuples contain simple data (item) but they cannot be updated nor edited. Several tuples can be mixed.

# E.g. as working days and weekend days are 5 and 2, these tuples should not be updated. They can be added.
days = weekdays + weekends

#########

# Dictionary
countries = {
    "Canada": {
        "capital": "Ottawa",
        "continent": "North America"
    },
    "France": {
        "capital": "Paris",
        "continent": "Europe"
    },
    "Kazakhstan": {
        "capital": "Astana",
        "continent": "Asia"
    }
}

# Dictionaries contain much more complex data, namely items (keys) and sub-items (values) which can be updated.
# E.g. countries can have more specific information which have been showed using a dictionary above.
# ALl data type can contain another data type which is shown in the "countries" dictionary. Each values can be edited.
countries["Kazakhstan"]["capital"] = "Nur-Sultan"

#########

# We can always access the information inside these data types.
print("I want to travel France, which is located in " + countries["France"]["continent"])
print("I am going to reach " + countries["France"]["capital"] + " on " + days[3] + " on an " + transports[0] + "\n")

#########

# zip() can be used to merge items of two different lists or tuples according to their index.
# since dictionaries do not have index but key, they cannot be merged using this function.
isDayOff = [True, True, True, True, True, False, False]

week = zip(days, isDayOff)
print("Output with zip:", tuple(week), "\n")

# zipped data can be displayed in different ways:
# print(list(week))   # displays as a list of tuples
# print(tuple(week))  # displays as a tuple of tuples
# print(dict(week))   # displays as a dictionary

#########

# enumerate() is used to numerate the items of either list or tuple.
# Starting number can be assigned as a second argument.
week = enumerate(days, 1)
print("Output with enumerate:", tuple(week), "\n")

# enumerated data can be displayed in different ways: refer to lines 59-61

#########

# items() method is used to convert the dictionary into a view object with all keys and values.
friendsAge = {
    "Farrukh": 19,
    "Anvar": 18,
    "Nilufar": 20
}
myFriends = friendsAge.items()
print("Output with items:", tuple(myFriends), "\n")

# Converted data can be displayed in different ways: refer to lines 59-61


