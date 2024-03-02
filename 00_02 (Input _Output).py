# ask the user for their name
username = input("What is your name? ")

# ask the user for their favourite number (integer)
fav_num = int(input("What is your favourite number? "))

# Double, halve and square the users favourite number
double = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num

# Greet the user
print(f"\nGday {username}, your favourite number is: {fav_num}")

# Output the results of doubling, halving and
# squaring their favourite integer
print(f"Doubling your favourite number is equal to {double} ")
print(f"Halving your favourite number is equal to {halve} ")
print(f"Squaring your favourite number is equal to {square} ")
print(f"Thank you for your time, {username}!")