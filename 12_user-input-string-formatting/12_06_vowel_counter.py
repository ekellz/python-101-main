# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

get_string = input("Please enter a phrase. ")

vowel_counts = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

for letter in get_string:
    if letter.lower() in vowel_counts:
        vowel_counts[letter.lower()] += 1
print(vowel_counts)