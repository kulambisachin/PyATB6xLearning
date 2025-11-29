"""
Program to find out the max of 3 no's

"""

# Step 1: Building Logic
# i/p: num1, num2, num3
# o/p: int datatype

# Step2: Rough logic
# Use input function for all the num1,num2, num3
# Use if-else and eif condition to check which is greater out of 3 no's
# 5 > 3 and 5 > 2 -> 5
# num1 > num2 and num1 > num3 -> num1
# num2 > num1 and num2 > num3 -> num2
# num3 -> max

num1 = int(input("Enter the input value of num1: ").strip())
num2 = int(input("Enter the input value of num2: ").strip())
num3 = int(input("Enter the input value of num3: ").strip())

if num1 >= num2 and num1 >= num3:
    print("num1 is greater")
elif num2 >= num1 and num2 >= num3:
    print("num2 is greater")
else:
    print("num3 is greater")
