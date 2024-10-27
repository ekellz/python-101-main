# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.

# What dish can you make from these ingredients? :)
    ## Apple pie, yummm :)

s = "They grappled with their leggins before going to see the buttercups flourish."

food_one = s[-9:-4:1]
print(food_one)
food_two = s[-20:-14:1]
print(food_two)
food_three = s[7:12:1]
print(food_three)
food_four = s[26:29:1]
print(food_four)