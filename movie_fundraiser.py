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
                current_user_list[0] = user_name
                return user_name
            else:
                # If spaces = 0, it prints error and asks again
                print(error)


def ticket_price_amount(question, error, error_2):
    global cost
    global t_amount
    cost = 0
    count = 1
    t_amount = 0
    valid = False
    valid_ticket_amount = False
    tickets_available = 3
    # Tells user how many tickets are available
    print("There are {} tickets available".format(tickets_available))
    # Asks how many tickets user wants
    while not valid:
        try:
            while not valid_ticket_amount:
                t_amount = int(input(question))
                if t_amount > tickets_available:
                    print(error_2)
                    print("There are {} tickets available".format(tickets_available))
                else:
                    valid_ticket_amount = True
                    current_user_list[1] = t_amount
                    print()

            while count < t_amount + 1:
                try:
                    # Asks for age
                    age = int(input("What age will ticket {} be for?".format(count)))
                    if age <= 11:
                        # If too young, user will be re_asked
                        print(error)
                    elif age >= 131:
                        # If too old, user will be re-asked
                        print(error)
                    else:
                        if age < 16:
                            print("Ticket {} will cost $7.50\n".format(count))
                            cost += 7.5
                            count += 1
                        elif 16 <= age <= 64:
                            print("Ticket {} will cost $10.50\n".format(count))
                            cost += 10.5
                            count += 1
                        else:
                            print("Ticket {} will cost $6.50\n".format(count))
                            cost += 6.5
                            count += 1
                except ValueError:
                    print(error)
                valid = True
        except ValueError:
            print(error)
    current_user_list[2] = cost
    print("Total cost of all tickets is ${:.2f}".format(cost))


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
                        print("And your choice was {} {}".format(user_snack_amount, snack_choices[user_choice - 1]))
                        if user_choice == 1:
                            current_user_list[3] += user_snack_amount
                            summary_details[1] += user_snack_amount
                        elif user_choice == 2:
                            current_user_list[4] += user_snack_amount
                            summary_details[2] += user_snack_amount
                        elif user_choice == 3:
                            current_user_list[5] += user_snack_amount
                            summary_details[3] += user_snack_amount
                        elif user_choice == 4:
                            current_user_list[6] += user_snack_amount
                            summary_details[4] += user_snack_amount
                        else:
                            current_user_list[7] += user_snack_amount
                            summary_details[5] += user_snack_amount
                        options = True
            elif yes_no == "n" or yes_no == "no":
                # Prints total price of all ordered snacks
                print("Total price of your snacks is: ${}".format(snack_price_total))
                cost += snack_price_total
                current_user_list[8] = snack_price_total
                return snack_price_total
        except ValueError:
            print(error)


def payment(question, error):
    global cost
    global payment_method
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
                current_user_list[9] = payment_method
                return payment_method
            elif payment_method == 2:
                # 2 corresponds to credit payment
                payment_method = "Credit"
                cost += cost * 0.05
                current_user_list[9] = payment_method
                return payment_method
            else:
                print(error)
        except ValueError:
            print(error)


def profit():
    global t_amount
    global profit_per_user
    profit_per_user = 0
    # Times profit per ticket by amount of tickets
    profit_per_user += 5.5 * t_amount
    summary_details[0] += profit_per_user


# Main routine
global cost
global t_amount
global profit_per_user
global payment_method
current_user_list = ["Name", "ticket amount", "total ticket price", 0, 0, 0, 0, 0,
                     "snack price", "payment method", "total price"]
summary_details = [0, 0, 0, 0, 0, 0]
not_blank("What is your name?", "Please enter a valid full name(first and last name)")
ticket_price_amount("How many tickets would you like?", "Please enter a valid age",
                    "Please enter a valid ticket amount")
snacks("Do you want to order some/more snacks?", "Pick a snack(pick the number you want)\nThe options are:\n"
       "1. Popcorn: $2.50\n2. M&M: $3.00\n"
       "3. Pitachips: $4.50\n4.Orange Juice: $3.25\n5. Water: $2.00", "Choose an amount(maximum is 5)",
       "Please enter a valid snack number")
payment("Will you be paying cash or credit?(enter 1 or 2)\nIf paying with credit "
        "there will be a surcharge of 2% to the final price\nOption 1                "
        "Option 2\nCash                    Credit", "Please enter a valid input(1 or 2)"
        "\nOption 1                "
        "Option 2\nCash                    Credit")
profit()
current_user_list[10] = cost
print("Total cost = ${:.2f}".format(cost))
print("Profit = ${:.2f}".format(profit_per_user))
print(current_user_list)
print(summary_details)
