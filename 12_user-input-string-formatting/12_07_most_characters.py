# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings
string_1 = input("Please enter some words. ")
string_2 = input("Please enter some more words. ")
string_3 = input("And three times a charm...more words please! ")

strings = [string_1, string_2, string_3]
strings.sort(key=len, reverse=True)

for i in strings:
    print(i)