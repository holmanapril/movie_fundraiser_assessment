# Functions
def ticket_price(question, error, error_2):
    global cost
    cost = 0
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
                if age < 16:
                    cost += 7.5
                    print(cost)
                elif 16 <= age <= 64:
                    cost += 10.5
                    print(cost)
                else:
                    cost += 6.5
                    print(cost)
                # If valid age, code finishes
                print(age)
                return age
        except ValueError:
            # Prints error message if string is input
            print(error)


def snacks(question_1, question_2, question_3, error):
    global cost
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
                cost += snack_price_total
                return snack_price_total
        except ValueError:
            print(error)


def payment(question, error):
    global cost
    valid = False
    # Prints question
    print(question)
    while not valid:
        try:
            # Asks what payment method
            payment_method = int(input())
            if payment_method == 1:
                # 1 corresponds to cash payment
                payment_method = "Cash"
                return payment_method
            elif payment_method == 2:
                # 2 corresponds to credit payment
                payment_method = "Credit"
                cost += cost * 0.05
                return payment_method
            else:
                print(error)
        except ValueError:
            print(error)


# Main routine
global cost
ticket_price("How old are you?", "Please enter a valid age between(12 and 130)",
             "You are too young to be doing this")
snacks("Do you want to order some/more snacks?", "Pick a snack(pick the number you want)\nThe options are:\n"
       "1. Popcorn: $2.50\n2. M&M: $3.00\n"
       "3. Pitachips: $4.50\n4.Orange Juice: $3.25\n5. Water: $2.00", "Choose an amount(maximum is 5)",
       "Please enter a valid snack number")
payment("Will you be paying cash or credit?(enter 1 or 2)\nIf paying with credit "
        "there will be a surcharge of 2% to the final price\nOption 1                "
        "Option 2\nCash                    Credit", "Please enter a valid input(1 or 2)"
        "\nOption 1                "
        "Option 2\nCash                    Credit")

print(cost)
