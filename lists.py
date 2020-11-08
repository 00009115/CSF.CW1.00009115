# List
transports = ["airplane", "train", "car", "bus", "ferry"]

# Lists contain simple data (item) and can be edited afterwards.

# E.g. as transport types are not as limited as in this list, it can be updated by adding or removing.
transports.append("helicopter")

# zip() can be used to merge items of two lists according to their index.
type_of_transport = ["air", "ground", "ground", "ground", "water", "air"]
transportation_options = list(zip(transports, type_of_transport))

print("\nZipping:")

for transport in transportation_options:
    print(transport[0], "-", transport[1])

# We can set index numbers to the each item of lists using enumerate() function

print("\nEnumerating:")
ordered_transports = list(enumerate(transports, 1))  # Second parameter sets the starting point of enumerating.

for transport in ordered_transports:
    print(str(transport[0]) + ")", transport[1])
