# VOID FUNCTIONS
# void functions do not return any value after being executed

message = ''


def check_age_void(age):
    global message

    if age < 18:
        message = "You are " + str(age) + " years old, thus not eligible for the installment."
    elif age >= 18:
        message = "You are " + str(age) + " years old and eligible to receive an installment."
    print(message)


# Now the function above should be executed separately in order to update the message to be printed.
if __name__ == '__main__':
    check_age_void(16)

# To avoid that, we can use value-returning functions which are shown below:


# VALUE RETURNING FUNCTIONS

def check_age_value(age):
    if age < 18:
        return "You are " + str(age) + " years old, thus not eligible for the installment."
    elif age >= 18:
        return "You are " + str(age) + " years old and eligible to receive an installment."

# Now we can use the function as an argument of print() function as it returns string value


print(check_age_value(20))

