from lists.lists import transports
from tuples.tuples import days
from dictionaries.dictionaries import countries

# We can always the access all types of data and use the items inside of them.
# Python runs all statements of certain file while importing the modules from it which caused more output in this file,

print("\nI want to travel France, which is located in", countries["France"]["continent"])
print("I am going to reach", countries["France"]["capital"], "on", days[3], "on an", transports[0])
