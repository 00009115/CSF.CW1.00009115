# Tuple
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
weekends = ("Saturday", "Sunday")

# Tuples contain simple data (item) but they cannot be updated nor edited. Several tuples can be mixed.

# E.g. as working days and weekend days are 5 and 2, these tuples should not be updated. They can be added.
days = weekdays + weekends

# zip() can be used to merge items of two tuples according to their index.
isDayOff = [True, True, True, True, True, False, False]
week = tuple(zip(days, isDayOff))

print("\nZipping:")

for x in week:
    if x[1]:  # This statement returns True which makes typing it unnecessary
        print(x[0] + " - business day")
    else:     # Else case of True is False, which makes writing elif statement unnecessary
        print(x[0] + " - day off")

# We can set index numbers to the each item of tuples using enumerate() function

print("\nEnumerating:")
ordered_days = tuple(enumerate(days, 1))  # Second parameter sets the starting point of enumerating.

for day in ordered_days:
    print(str(day[0]) + ")", day[1])
