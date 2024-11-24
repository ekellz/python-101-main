# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib

path = pathlib.Path("/Users/ericajansen/Documents/Coding Projects/single-scripts")

for filepath in path.rglob("*.py"):
    print(filepath.name)






