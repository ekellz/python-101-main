# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

string = input("Please enter some word or phrase. ")
new_letter = input("Please pick a new symbol. ")
replace_letter = input("What letter would you like to replace? ")

# Find the replacement letter
#index = string.find(replace_letter)

# Replace the letter
new_string = string.replace(replace_letter, new_letter)
print(new_string)
