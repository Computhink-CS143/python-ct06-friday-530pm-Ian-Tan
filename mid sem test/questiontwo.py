# Ask for the starting amount of money.
# Ask for the number of days.
# For each day, add the correct savings amount.
# Print the total money after each day.
# Finally, print the final total amount.

startingAmount = input("what is the starting amount?")
NumOfDays = input("how many days do you want to save it?")
startingAmount = int(startingAmount)
NumOfDays = int(NumOfDays)
addEachDay = 0
count2 = 0
for count in range(1,(NumOfDays+1)):
    addEachDay = int(addEachDay) + (1 + count2)
    count2 = count2 + count
    print("Day " , count , ": $" , (startingAmount + addEachDay))
print("total amount saved = $" , startingAmount + addEachDay)