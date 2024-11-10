# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

user_opinion = input("Oh, please...do tell ;). ")

alternating_opinion = ""
toggle = True

for char in user_opinion:
    if char.isalpha():
        if toggle: 
            alternating_opinion += char.upper()
        else:
            alternating_opinion += char.lower()
        toggle = not toggle
    else:
        alternating_opinion += char

print(alternating_opinion)

