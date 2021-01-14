# Functional
def display_operation_func(name, balance, spent, gender):  # function has 4 parameters

    # Identifying the pronoun that will be used in the messages
    if gender == "male":
        pronoun = "his"
    elif gender == "female":
        pronoun = "her"
    else:
        pronoun = "their"

    print("Client ", name, "spent an amount of", spent, "and", pronoun, "current balance is", balance-spent, "\n")


display_operation_func("Yodgorov", 3750000, 250000, "female")  # calling the functions with arguments


# OOP
class User:

    # creating a class which can be used to build new objects with the same structure
    def __init__(self, name, balance, spent, gender):
        self.name = name
        self.balance = balance
        self.spent = spent
        self.gender = gender

    def identify_pronoun(self):
        if self.gender == "male":
            return "His"
        elif self.gender == "female":
            return "Her"
        else:
            return "Their"

    def update_balance(self):
        self.balance -= self.spent

    def say_operation(self):
        print("Client ", self.name, "spent an amount of",
              self.spent)

    def say_balance(self):
        print(self.identify_pronoun(), "current balance is", self.balance)


if __name__ == "__main__":

    # building the first object
    user_1 = User("Bakhodirov", 1500000, 84000, "male")
    user_1.update_balance()
    user_1.say_operation()
    user_1.say_balance()

    print('\n')

    # building the second object
    user_2 = User("Azimova", 550000, 39000, "female")
    user_2.update_balance()
    user_2.say_operation()
    user_2.say_balance()