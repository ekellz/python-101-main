# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "
word_one = word[1:3:1]
#print(word_one)
word_two = word[-2:-7:-2]
#print(word_two)
word_three = word[0] + word[-3] + word[2:4:1] + word[-2]
print(word_three)

print(f"{word_one}   {word_two}  {word_three}")