# List
transports = ["airplane", "car", "ferry"]
modes = ["air", "ground", "water"]

# Lists contain simple data (index based item) and can be edited after being assigned.
# E.g. as transport types are not as limited as in this list, it can be updated by adding or removing.

# Let's create a couple of functions for adding and removing items, and use them.
print("\nLIST DATA TYPE")
print("--------------\n")   # just for formatting the output in order to keep it clean


# Adding items to the list

def add_transport():   # first parameter is for the name, second one is for the mode of the transport
    global transports
    global modes

    message = input("Do you want to ADD a new transport? [Type yes/no]: ").lower().strip()
    # validating the input by lower-casing the letters and shrinking the spaces

    if message == "yes":
        name = input(" Insert the transport name: ")

        if name in transports:
            print("\n!!! This transport is already in the list\n")
            add_transport()
        else:
            mode = input(" Insert the transportation mode: ")
            transports.append(name)   # append() method is used to add a new item
            modes.append(mode)

        print("\nSuccessfully added!")
        print("--------------\n")  # just for formatting the output in order to keep it clean
        add_transport()
    elif message == "no":
        print("--------------\n")  # just for formatting the output in order to keep it clean
        return
    else:
        print("\n!!! Please, answer properly\n")
        add_transport()


add_transport()   # calling the function to add a new transport


# Removing items from the list

def remove_transport():   # receives an integer as an index
    global transports
    global modes

    message = input("Do you want to REMOVE any transport? [Type yes/no]: ").lower().strip()
    # validating the input by lower-casing the letters and shrinking the spaces

    if message == "yes":
        print("You have the transports below:")

        for number, transport in enumerate(transports, 1):   # looping the enumerated list to print the items
            print("", str(number) + ")", transport)

        removing_index = input("Insert the number of the transport you want to delete: ")

        try:   # trying to convert the input into integer
            index = int(removing_index)
            transports.pop(index - 1)   # since enumeration has started with 1, we should subtract 1
            modes.pop(index - 1)
            print("\nSuccessfully removed!")
            print("--------------\n")  # just for formatting the output in order to keep it clean
            remove_transport()
        except ValueError:
            print("\n!!! Please, insert only numbers\n")
            remove_transport()
    elif message == "no":
        print("--------------\n")  # just for formatting the output in order to keep it clean
        return
    else:
        print("\n!!! Please, answer properly\n")
        remove_transport()


remove_transport()   # calling the function to remove an existing transport


# Check the type of the transport
# zip() can be used to merge relative items of two lists according to their index.

def check_transport():
    global transports
    global modes

    message = input("Do you want to CHECK the mode of any transport? [Type yes/no]: ").lower().strip()
    # validating the input by lower-casing the letters and shrinking the spaces

    if message == "yes":
        print("Choose a transport to check:")

        for number, transport in enumerate(transports, 1):
            print("", str(number) + ")", transport)

        checking_index = input("Insert the number of the transport you want to check: ")

        try:
            index = int(checking_index)
            print("\n", transports[index-1][0].upper() + transports[index-1][1:], "moves on the", modes[index-1] + ".")
            print("--------------\n")  # just for formatting the output in order to keep it clean
            check_transport()
        except ValueError:
            print("\n!!! Please, insert only numbers!\n")
            check_transport()
    elif message == "no":
        print("--------------\n")  # just for formatting the output in order to keep it clean
        print(" Thank you for using this app! Good bye!")
        return
    else:
        print("\n!!! Please, answer properly!\n")
        check_transport()


check_transport()  # calling the function to check the mode af a transport
