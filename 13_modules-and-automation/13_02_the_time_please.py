# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.

import datetime
now = datetime.datetime.now()
current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
print(current_datetime)