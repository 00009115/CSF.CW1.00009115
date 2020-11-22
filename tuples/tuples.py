# Tuple
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
weekends = ("Saturday", "Sunday")

# Tuples contain simple data (index based items) but they cannot be updated nor edited. Several tuples can be mixed.
# E.g. as working days and weekend days are 5 and 2, these tuples should not be updated. They can be added.
days = weekdays + weekends

# Let's create a function using the tuples above simultaneously.
print("\nTUPLE DATA TYPE")
print("--------------\n")   # just for formatting the output in order to keep it clean


# The function below is meant to identify if the day inserted is day-off or working-day.

def check_day():
    global days

    message = input("Do you want to check if certain day is day off? [Type yes/no]: ").lower().strip()
    # validating the input by lower-casing the letters and shrinking the spaces

    if message == "yes":
        print("Choose a day to check:")

        for number, day in enumerate(days, 1):   # looping the enumerated tuple to print the items
            print("", str(number) + ")", day)

        checking_index = input("Insert the number of the day you want to check: ")

        try:   # trying to convert the input into integer
            index = int(checking_index)
            if 1 <= index <= 5:   # since 1-5 days are working days
                print("\n Eh,", days[index - 1], "is a working-day. Be patient :(")
            elif 6 <= index <= 7:   # since 6-7 days are days-off
                print("\n Yay,", days[index - 1], "is a day-off. Enjoy :)")
            else:   # for validating the input
                print("\n!!! Please, insert a number between 1-7!\n")

            print("--------------\n")  # just for formatting the output in order to keep it clean
            check_day()
        except ValueError:   # if the input cannot be converted to int, then it is not valid.
            print("\n!!! Please, insert only numbers!\n")
            check_day()
    elif message == "no":
        print("--------------\n")  # just for formatting the output in order to keep it clean
        return
    else:   # for validating the input
        print("\n!!! Please, answer properly!\n")
        check_day()


check_day()  # calling the function to check if a day is day-off

# Let's try zip() function with tuples after creating a tuple of ordered lessons day by day.

lessons = (("CSF", "IMOB"), ("WebTech", "ISDS"), ("IMOB", "CSF"), "FunPro", "ISDS", "", "")
timetable = tuple(zip(days, lessons))   # zipping two tuples into another tuple


# The function below is meant to show the timetable of the specific day.

def check_timetable():
    global days
    global timetable

    message = input("Do you want to check timetable of a specific day? [Type yes/no]: ").lower().strip()
    # validating the input by lower-casing the letters and shrinking the spaces

    if message == "yes":
        print("Choose a day:")

        for number, day in enumerate(days, 1):
            print("", str(number) + ")", day)

        checking_index = input("Insert the number of the day you want to check: ")

        try:
            index = int(checking_index)

            if 1 <= index <= 7:   # ranging between 1-7 because we have only 7 week days
                classes = timetable[index - 1][1]
                if isinstance(classes, str) and classes:   # checking whether it is string and not empty / if one class
                    print("\n You have only", classes, "class on", timetable[index - 1][0] + ".")
                elif isinstance(classes, list) or isinstance(classes, tuple):   # if several classes
                    print("\n You have", classes[0], "and", classes[1], "classes on", timetable[index - 1][0] + ".")
                elif not classes:   # if no class
                    print("\n You don't have any lessons on", timetable[index - 1][0], ":)")
                print("--------------\n")  # just for formatting the output in order to keep it clean
                check_timetable()
            else:
                print("\n!!! Please, insert a number between 1-7!\n")
                check_timetable()

        except ValueError:
            print("\n!!! Please, insert only numbers!\n")
            check_timetable()
    elif message == "no":
        print("--------------\n")  # just for formatting the output in order to keep it clean
        print(" Thank you for using this app! Good bye!")
        return
    else:
        print("\n!!! Please, answer properly!\n")
        check_timetable()


check_timetable()  # calling the function to check the mode af a transport
