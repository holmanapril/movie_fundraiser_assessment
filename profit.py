def ticket_price_amount(question, error, error_2):
    global t_amount
    global cost
    cost = 0
    count = 1
    t_amount = 0
    valid = False
    valid_ticket_amount = False
    tickets_available = 3
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
                            # Different price for younger people
                            print("Ticket {} will cost $7.50\n".format(count))
                            cost += 7.5
                            count += 1
                        elif 16 <= age <= 64:
                            # Different price for middle ages
                            print("Ticket {} will cost $10.50\n".format(count))
                            cost += 10.5
                            count += 1
                        else:
                            # Different price for elderly
                            print("Ticket {} will cost $6.50\n".format(count))
                            cost += 6.5
                            count += 1
                except ValueError:
                    print(error)
                valid = True
        except ValueError:
            print(error)
    print("Total cost of all tickets is ${:.2f}".format(cost))


def snacks(question_1, question_2, question_3, error):
    global profit_per_user
    profit_per_user = 0
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
                profit_per_user += snack_price_total * 0.2
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


def profit():
    global cost
    global t_amount
    global profit_per_user
    profit_per_user += 5.5 * t_amount


# Main routine
global cost
global t_amount
global profit_per_user
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
print("Total cost = ${:.2f}".format(cost))
print("Profit = ${:.2f}".format(profit_per_user))
