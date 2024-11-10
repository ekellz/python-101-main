# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

get_num = input("Please type a number between 1 and 1,000,000,000. ")
num = int(get_num)

if num % 3 == 0:
    print(num)
else:
    print("Your number is not divisible by 3. ")