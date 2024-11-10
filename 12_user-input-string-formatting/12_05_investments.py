# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

get_investment_amount = input("Please enter the amount to invest. ")
investment_amount = int(get_investment_amount)
get_interest_rate = input("Please enter an interest rate. ")
interest_rate = float(get_interest_rate)
get_years_to_invest = input("How many years would you like to invest? ")
years_to_invest = int(get_years_to_invest)

# Calculations
future_value = (investment_amount * interest_rate) * years_to_invest
print(f"Your investment would reach $550{future_value}. ")