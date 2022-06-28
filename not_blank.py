# Functions
def not_blank(question, error):
    valid = False
    # Keeps running loop until user inputs a valid name
    while not valid:
        count = 0
        # Asks question
        user_name = str(input(question)).title().strip()
        # Counts how many spaces there are in user_name
        for i in range(len(user_name)):
            if user_name[i].isspace():
                count += 1
        print(count)
        # Doesn't let user enter a name that has
        if count <= 0:
            print(error)
        else:
            # Makes sure input isn't a number or blank
            if user_name.isalpha() is False or user_name.isnumeric() or user_name == "":
                # If digit or blank, error message prints
                print(error)
            else:
                print(user_name)
                return user_name


# Main Routine
not_blank("What is your name?", "Please enter a valid full name(first and last name)")
