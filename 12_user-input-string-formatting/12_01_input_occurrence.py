# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

string = input("Please enter some word. ")
letter = input("Please pick a random letter from your prior word. ")

index = string.find(letter)

if index != -1:
    print(f"It's at {index}")
else: 
    print("put yo stuff in right")