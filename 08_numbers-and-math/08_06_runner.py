# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

# Calculate average

miles_ran = 10
minutes_ran = 30
seconds_ran = 30
minutes_per_hour = 60

# Convert to kilometers
kilometers_ran = 10 * 1.6

# Convert to minutes
total_minutes = minutes_ran + seconds_ran / minutes_per_hour

# Convert to hourly
total_hours = total_minutes / minutes_per_hour

# Calculate the average
average = kilometers_ran / total_hours
print(f"average = {average}")
