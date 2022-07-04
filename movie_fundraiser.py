# Functions
def not_blank(question, error):
    valid = False
    # Asks user what their name is
    print(question)
    # Keeps asking user until valid input entered
    while not valid:
        # stores input as user_name
        user_name = str(input()).title().strip()
        # Counts the amount of spaces after strip()
        spaces = (user_name.count(" "))
        # Replaces space with no space
        user_name_no_space = user_name.replace(" ", "")
        # Checks if user_name is all letter and isn't blank
        if user_name_no_space.isalpha() is False or user_name_no_space == "":
            # If user_name is not valid input, error message printed
            print(error)
        else:
            # Checks amount of spaces
            if spaces >= 1:
                # If spaces is more than 0, it reprints name and ends the function
                print(user_name)
                return user_name
            else:
                # If spaces = 0, it prints error and asks again
                print(error)


def user_age(question, error, error_2):
    valid = False
    # Continues to ask for input until valid input it entered
    while not valid:
        try:
            # Asks for age
            age = int(input(question))
            if age <= 11:
                # If too young, code will finish
                print(error_2)
                return age
            elif age >= 131:
                # If too old, user will be re-asked
                print(error)
            else:
                # If valid age, code finishes
                print(age)
                return age
        except ValueError:
            # Prints error message if string is input
            print(error)


def ticket_price(question, error):
    cost = 0
    age = 0
    # Asks user what their age is
    print(question)
    valid = False
    while not valid:
        try:
            age = int(input())
            # If age is less than 16 the code finishes
            if age < 16:
                cost += 7.5
                valid = True
            # if age between 16 and 64 cost = 10.5 and finishes
            elif 16 <= age <= 64:
                cost += 10.5
                valid = True
            else:
                cost += 6.5
                valid = True
        # If invalid input is entered error message is printed
        except ValueError:
            print(error)
    print(age)
    print(cost)


# Main Routine
not_blank("What is your name?", "Please enter a valid full name(first and last name)")
user_age("How old are you?", "Please enter a valid age between(12 and 130)",
         "You are too young to be doing this")
ticket_price("How old are you?", "Please enter a valid age")
