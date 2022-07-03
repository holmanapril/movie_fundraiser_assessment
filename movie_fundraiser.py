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


# Main Routine
not_blank("What is your name?", "Please enter a valid full name(first and last name)")