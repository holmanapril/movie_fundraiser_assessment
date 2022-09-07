def ticket_price_amount(question, error, error_2):
    cost = 0
    count = 1
    t_amount = 0
    valid = False
    valid_ticket_amount = False
    tickets_available = 7
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
    print("Total cost of all tickets is ${:.2f}".format(cost))


ticket_price_amount("How many tickets would you like?", "Please enter a valid age",
                    "Please enter a valid ticket amount")
