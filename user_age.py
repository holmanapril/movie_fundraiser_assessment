# Asks for users age
age = int(input("How old are you?"))
if age <= 11:
    # User too young
    print("You are too young to be doing this")
elif age >= 131:
    # User too old
    print("Please enter a valid age between(12 and 130)")
else:
    # valid age
    print(age)
