# Functions
def snacks(question, error, question_2, error_2, question_3):
    # Snack choices
    snack_choices = ["Popcorn", "M&M", "Pitachips", "Orangejuice", "Water"]
    keep_going = False
    # Keeps asking if user wants more snacks
    while keep_going is False:
        # Asks if user want snacks
        snack_yes_no = str(input(question_3)).lower().strip()
        if snack_yes_no == "y" or snack_yes_no == "yes":
            valid = False
            print(question)
            while not valid:
                # What snacks are wanted
                user_choice = str(input()).title().strip()
                if user_choice not in snack_choices:
                    print(error)
                else:
                    # Reprints users input to check
                    print(user_choice)
                    valid = False
                    while not valid:
                        try:
                            # Asks how many loops until valid input entered
                            user_snack_amount = int(input(question_2))
                            if user_snack_amount <= 0:
                                print(error_2)
                            # Limit is 5
                            elif user_snack_amount >= 6:
                                print(error_2)
                            else:
                                print(user_snack_amount)
                                valid = True
                        except ValueError:
                            print(error_2)
        else:
            # if user answers no code finishes
            keep_going = True


# Main routine
snacks("What snack would you like?", "Please enter a valid snack choice(Please do not put spaces between words",
       "How many would you like?", "Please enter a valid amount(The maximum you can order of each snack is 5)",
       "Would you like to order any/more snacks?\nThe Options are:\nPopcorn\nM&M\nPita chips\nOrange Juice\nWater?")
