import pandas as pd


# Functions
def decoration(greeting, symbol):
    sides = symbol
    greeting = "{} {} {}".format(sides, greeting, sides)
    top_bottom = symbol * len(greeting)
    print(top_bottom)
    print(greeting)
    print(top_bottom)


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
                print("Welcome, {}".format(user_name))
                one_ticket[0] = user_name
                return user_name
            else:
                # If spaces = 0, it prints error and asks again
                print(error)


def ticket_price_amount(question, error, error_2):
    global cost
    global t_amount
    global tickets_available
    cost = 0
    count = 1
    t_amount = 0
    valid = False
    valid_ticket_amount = False
    # Tells user how many tickets are available
    print("\nThere are {} tickets available,".format(tickets_available))
    # Asks how many tickets user wants
    while not valid:
        try:
            while not valid_ticket_amount:
                t_amount = int(input(question))
                if t_amount > tickets_available:
                    print(error_2)
                    print("There are {} tickets available".format(tickets_available))
                else:
                    tickets_available -= t_amount
                    valid_ticket_amount = True
                    one_ticket[1] = t_amount
                    print()

            while count < t_amount + 1:
                try:
                    # Asks for age
                    age = int(input("What age will Ticket {} be for?".format(count)))
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
    one_ticket[2] = cost
    print("Total cost of all tickets = ${:.2f}\n".format(cost))


def snacks(question_1, question_2, question_3, error, error_2):
    global cost
    global snack_price_total
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
                    if user_choice > 5 or user_choice < 1 or user_snack_amount > 5 or user_snack_amount < 1:
                        print(error)
                    else:
                        # Calculates snack pricing
                        snack_price = snack_prices[user_choice - 1] * user_snack_amount
                        # Adds to total
                        snack_price_total += snack_price
                        # Prints choices to and price
                        print("You chose {} {}\nCost = ${:.2f}".format(user_snack_amount,
                                                                       snack_choices[user_choice - 1], snack_price))
                        if user_choice == 1:
                            one_ticket[3] += user_snack_amount
                            if one_ticket[3] >= 6:
                                one_ticket[3] -= user_snack_amount
                                print(error_2)
                            summary_details[0][1] += user_snack_amount
                        elif user_choice == 2:
                            one_ticket[4] += user_snack_amount
                            if one_ticket[4] >= 6:
                                one_ticket[4] -= user_snack_amount
                                print(error_2)
                            summary_details[0][2] += user_snack_amount
                        elif user_choice == 3:
                            one_ticket[5] += user_snack_amount
                            # Stops user from ordering more than 5 of any type of snack
                            if one_ticket[5] >= 6:
                                one_ticket[5] -= user_snack_amount
                                print(error_2)
                            summary_details[0][3] += user_snack_amount
                        elif user_choice == 4:
                            one_ticket[6] += user_snack_amount
                            if one_ticket[6] >= 6:
                                one_ticket[6] -= user_snack_amount
                                print(error_2)
                            summary_details[0][4] += user_snack_amount
                        else:
                            one_ticket[7] += user_snack_amount
                            if one_ticket[7] >= 6:
                                one_ticket[7] -= user_snack_amount
                                print(error_2)
                            summary_details[0][5] += user_snack_amount
                        options = True
            elif yes_no == "n" or yes_no == "no":
                cost += snack_price_total
                one_ticket[8] = snack_price_total
                # Prints snack choices in easy to read way
                print("Your snack choices are:\n")
                print("Popcorn   M&M's   Pita Chips   Orange Juice   Water")
                print("  {}        {}          {}             {}           {}".format(one_ticket[3], one_ticket[4],
                                                                                      one_ticket[5], one_ticket[6],
                                                                                      one_ticket[7]))
                # Prints total price of all ordered snacks
                print()
                decoration("Total price of your snacks is: ${}".format(snack_price_total), "-")
                print()
                return snack_price_total
        except ValueError:
            print(error)


def payment(question, error):
    global cost
    global payment_method
    global user_will_pay
    global one_ticket
    global confirm_user_pays
    user_will_pay = False
    valid = False
    # Prints question
    decoration("Payment", "*")
    print("Your order total is ${:.2f}\n".format(cost))
    while not valid:
        try:
            confirm_user_pays = str(input("Are you wanting to continue to payment?")).strip().lower()
            if confirm_user_pays == "n" or confirm_user_pays == "no":
                print()
                decoration("Have a nice rest of your day", "^")
                print("\n\n\n")
                one_ticket = []
                valid = True
            elif confirm_user_pays == "y" or confirm_user_pays == "yes":
                user_will_pay = True
                print(question)
                valid = False
                while not valid:
                    try:
                        # Asks what payment method
                        payment_method = int(input())
                        if payment_method == 1:
                            # 1 corresponds to cash payment
                            payment_method = "Cash"
                            one_ticket[9] = payment_method
                            one_ticket[10] = cost
                            valid = True
                            return payment_method
                        elif payment_method == 2:
                            # 2 corresponds to credit payment
                            payment_method = "Credit"
                            cost += cost * 0.05
                            one_ticket[10] = cost
                            one_ticket[9] = payment_method
                            valid = True
                            return payment_method
                        else:
                            print(error)
                    except ValueError:
                        print(error)
        except ValueError:
            print(error)


def profit():
    global user_will_pay
    global t_amount
    global profit_per_user
    global tickets_available
    global snack_price_total
    profit_per_user = 0
    if user_will_pay is True:
        # Times profit per ticket by amount of tickets
        profit_per_user += 5.5 * t_amount
        profit_per_user += 0.2 * snack_price_total
        summary_details[0][0] += profit_per_user
    else:
        tickets_available -= t_amount


# Main routine
global cost
global t_amount
global profit_per_user
global payment_method
global current_user_list
global user_will_pay
global snack_price_total
global confirm_user_pays
all_tickets = []
summary_details = [[0, 0, 0, 0, 0, 0]]
tickets_available = 10
while tickets_available > 0:
    # Using all of my functions
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.expand_frame_repr", False)
    one_ticket = ["Name", "ticket amount", "total ticket price", 0, 0, 0, 0, 0, "snack price",
                  "payment method", "total price"]
    current_user_list = []
    decoration("Movie Fundraiser", "*")
    not_blank("What is your name?", "Please enter a valid full name(first and last name)")
    ticket_price_amount("How many tickets would you like?", "Please enter a valid age/number\n",
                        "Please enter a valid ticket amount")
    snacks("\nDo you want to order some/more snacks?", "\nPick a snack(pick the number you want), "
           "if you no longer want to order snack press enter\n\nThe options are:\n"
           "1. Popcorn: $2.50\n2. M&M: $3.00\n"
           "3. Pitachips: $4.50\n4. Orange Juice: $3.25\n5. Water: $2.00", "Choose an amount(maximum is 5)",
           "Please enter a valid snack number(as a digit)", "Sorry, You can only order a total of 5 of each snack"
           "(because you ordered more than 5 the ones you just ordered will be deducted from your order)")
    payment("\nWill you be paying cash or credit?(enter 1 or 2)\nIf paying with credit "
            "there will be a surcharge of 2% to the final price\nOption 1                "
            "Option 2\nCash                    Credit", "Please enter a valid input(1 or 2)"
            "\nOption 1                "
            "Option 2\nCash                    Credit")
    if user_will_pay is True:
        profit()
        current_user_list.append(one_ticket)
        current_ticket = pd.DataFrame(current_user_list, columns=["Name", "Ticket Amount", "Total Ticket Price",
                                                                  "Popcorn", "M&M's", "Pita Chips", "Orange Juice",
                                                                  "Water", "Snack Price", "Payment method",
                                                                  "Order total"])
        # Prints formatted list
        print(current_ticket)
        print()
        decoration("Thank you, Have a good day", "*")
        all_tickets.append(one_ticket)
        print("\n\n\n\n")
    else:
        tickets_available += t_amount
print("\n\n\n")
# Formats all ticket details and summary using pandas
all_ticket_details = pd.DataFrame(all_tickets, columns=["Name", "Ticket Amount", "Total Ticket Price",
                                                        "Popcorn", "M&M's", "Pita Chips", "Orange Juice",
                                                        "Water", "Snack Price", "Payment method",
                                                        "Order total"])
total_summary = pd.DataFrame(summary_details, columns=["Profit", "Popcorn", "M&M's", "Pita Chips", "Orange Juice",
                                                       "Water"])
# Sends formatted lists to csv files
all_ticket_details.to_csv('ticket_details.csv', header=True)
total_summary.to_csv('summary_details.csv', header=True)
