"""
Write a program to check if a number entered by the user is greater than 100

"""

# Step 1: Building the logic
# i/p: num1 > 100
# o/p: int, float any data type

# Step 2: Rough Logic
# Using input function with int data type
# Adding the logic num>100 with if and else condition.

num = int(input("Enter the value of number: "))

if num > 100:
    print("User has entered number greater than 100")
else:
    print("User has the entered value less than 100")
