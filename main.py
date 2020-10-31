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


