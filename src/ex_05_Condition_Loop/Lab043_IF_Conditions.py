"""
Write a program to take a user age and let him know if he can go the club, #21
"""

# Step 1: Building the logic
# i/p: age variable in the as input
# o/p: user can go to club or not?

# Step 2: Rough logic
# Add an input function and if else to check whether user can go to club

age = int(input("Enter the user age: "))

if age >= 21:
    print("User can enter the club")
else:
    print("User cannot enter the club")

# Step 3: Handling the edge cases scenario:
