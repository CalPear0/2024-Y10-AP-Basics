# Ask user for width and loop until
# they enter a number that is more than 0
def num_check(question):
    error = "Please enter a number that or more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than 0
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine starts here

keep_going = ""
while keep_going == "":
        # Get width and height
        print("Please enter data below.\n")
        width = float(input("Width: "))
        height = float(input("Height: "))

        # Calculate area / perimeter
        area = width * height
        perimeter = 2 * (width + height)

        # Display output
        print(f"The Area is {area} units!")
        print(f"The Perimeter is {perimeter} square units!")

        # Ask user if they want to keep going

        keep_going = input("Enter = Continue | Any Key + Enter = Exit.")
        print()

print("Thank you for using this program.")