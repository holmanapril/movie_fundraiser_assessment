# Functions
def payment(question, error):
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
                return payment_method
            else:
                print(error)
        except ValueError:
            print(error)


# Main routine
payment("Will you be paying cash or credit?(enter 1 or 2)\nIf paying with credit "
        "there will be a surcharge of 2% to the final price\nOption 1                "
        "Option 2\nCash                    Credit", "Please enter a valid input(1 or 2)"
        "\nOption 1                "
        "Option 2\nCash                    Credit")
