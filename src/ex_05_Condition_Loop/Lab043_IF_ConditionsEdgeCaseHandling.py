"""
Check for the edge cases.
# We should consider edge cases such as:
# Negative ages or extremely high values -> program will break.
# Non-numeric input - ABC ( This is will be learnt during the try and catch exception)
# Age which is valid. > 130

"""

# Step 1: Building the logic
# i/p: age variable in the as input
# o/p: user can go to club or not?

# Step 2: Rough logic
# Add an input function and if else to check whether user can go to club


# Step 3.  Optimize the code.
# Handle all the edges.


age = float(input("Enter the value of age: ").strip())
# This will be trim the front and back spaces of value, if the user has given it.
# Also handles the float value given as an input

if age <= 0 or age >= 130:  # Negative ages or extremely high values
    print("Enter an valid age")
else:
    if age >= 21:  # Positive age cases
        print("User can enter the club")
    else:
        print("User cannot go the club")
