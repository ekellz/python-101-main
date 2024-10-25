# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?

# 1) Convert int to float
variable = 33
new_variable = float(variable)
print(new_variable)

# 2) Convert float to an int
variable = 33.90
int_variable = int(variable)
print(int_variable)

# 3) Division with float and int
float_variable_one = 10.5
float_variable_two = 2.0
float_answer = float_variable_one / float_variable_two
print(float_answer)

int_variable_one = 10
int_variable_two = 2
int_answer = int_variable_one / int_variable_two
print(int_answer)

# 4) Two variable multiplication
mult_one = 10
mult_two = 2.5
mult_answer = mult_one * mult_two
print(mult_answer)
