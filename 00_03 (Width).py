# Ask user for width and loop until
# they enter a number that is more than 0

error = "Please enter a number that or more than zero\n"
while True:

    try:
        # ask the user for a number
        width = float(input("Width: "))

        #check that the number is more than 0
        if width > 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)