# Ask the user for Total bill
# Ask the user for Number of people
# Calculate how much each person pays
# Print the result exactly in this format:
# Each person pays: $<amount>
# Note: The output must be rounded to 2 decimals places (example: $25.25).

bill = input("what is the total bill?")
NumberOfPeople = input("how many people are there?")
amount = round(int(bill)/int(NumberOfPeople) , 2)
print("Each person pays: $" + str(amount))