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


def snacks(question_1, question_2, question_3, error):
    snack_price_total = 0
    # Snack choices
    snack_choices = ["Popcorn", "M&M", "Pitachips", "Orangejuice", "Water"]
    # Snack prices
    snack_prices = [2.50, 3.00, 4.50, 3.25, 2.00]
    valid = False
    while not valid:
        options = False
        try:
            # Asks if more snacks wanted
            yes_no = str(input(question_1)).strip().lower()
            if yes_no == "y" or yes_no == "yes":
                while not options:
                    # User inputs corresponding number of snack
                    user_choice = int(input(question_2))
                    # User inputs snack amount
                    user_snack_amount = int(input(question_3))
                    # Errors if invalid input entered
                    if user_choice >= 5 or user_choice < 0 or user_snack_amount > 5 or user_snack_amount < 1:
                        print(error)
                    else:
                        # Calculates snack pricing
                        snack_price = snack_prices[user_choice - 1] * user_snack_amount
                        # Adds to total
                        snack_price_total += snack_price
                        # Prints snack price of snack just chosen
                        print("${:.2f}".format(snack_price))
                        # Prints choices to check
                        print("And your choices were {} {}".format(user_snack_amount, snack_choices[user_choice - 1]))
                        options = True
            elif yes_no == "n" or yes_no == "no":
                # Prints total price of all ordered snacks
                print("Total price of your snacks is: ${}".format(snack_price_total))
                return snack_price_total
        except ValueError:
            print(error)


# Main Routine
not_blank("What is your name?", "Please enter a valid full name(first and last name)")
user_age("How old are you?", "Please enter a valid age between(12 and 130)",
         "You are too young to be doing this")
ticket_price("How old are you?", "Please enter a valid age")
snacks("Do you want to order some/more snacks?", "Pick a snack(pick the number you want)\nThe options are:\n"
       "1. Popcorn: $2.50\n2. M&M: $3.00\n"
       "3. Pitachips: $4.50\n4.Orange Juice: $3.25\n5. Water: $2.00", "Choose an amount(maximum is 5)",
       "Please enter a valid snack number")
