# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

get_name = input("Please enter your name. ")
name = get_name.split()[0]
message = (f"Welcome, {name}! I much appreciate you utilziing my script! :) ")
print(message)


