# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

number = (input("Please enter a number between 1 and 12. "))
num = int(number)

if 1 <= num <= 12:
    months = ["start_List", "January", "February", "March"]
    month_name = months[num]
    print(month_name)
else:
    print("You did not enter an appropriate number. ")
