"""
Write a program to check whether the positive number is even or odd

"""

# Step 1: Building logic
# i/p: num is divisible by 2 or not to decide whether it is even or odd.
# o/p: int, float data type

# Step 2: Rough logic:
# Use the input function for entering the number.
# Use the formula  num % 2 == 0

num = float(input("Enter the number to check it is even or odd number: ").strip())

if num >= 0:
    if num % 2 == 0:
        print(" Number is even")
    else:
        print("Number is odd")
else:
    print("Number is negative number")
