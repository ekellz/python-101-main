# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

get_number = input("Please enter a number between 0 and 1,000,000,000. ")
num = int(get_number)

if 1 <= num <= 1000000000:
    number = 1
    while number <= num:
        if number == num:
            print(f"Your number is: {num}. ")
            break
        number += 1
else:
    print("Fix yo entry. ")
    

