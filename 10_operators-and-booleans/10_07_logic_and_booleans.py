# Demonstrate the use of all logical operators (and, or, not) below.
# Create variables that hold boolean values, then combine them
# to express the following sentence:
#
#   do two wrongs make a right?
# 
# Note that the truth value of the statement doesn't matter,
# but try to use all three logical operators in one line of code
# to get another boolean value as your result :)

wrong = False
right = True


print(wrong or right)
print(wrong or wrong)
print(right or right)
print(wrong and right)
print(right and right)
print(wrong and wrong)


not_wrong = not wrong
print(not_wrong)

not_right = not right
print(not_right)