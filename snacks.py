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
                    if user_choice > 5 or user_choice < 1 or user_snack_amount > 5 or user_snack_amount < 1:
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


snacks("Do you want to order some/more snacks?", "Pick a snack(pick the number you want)\nThe options are:\n"
       "1. Popcorn: $2.50\n2. M&M: $3.00\n"
       "3. Pitachips: $4.50\n4.Orange Juice: $3.25\n5. Water: $2.00", "Choose an amount(maximum is 5)",
       "Please enter a valid snack number")
