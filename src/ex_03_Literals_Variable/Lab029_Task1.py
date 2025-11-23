"""
Program to demonstrate the sum, mul, div of 3 numbers

"""

# Building logic

# i/p: num1, num2, num3
# o/p: sum, mul,div

num1 = float(input("Enter the 1st Number:"))
num2 = float(input("Enter the 2nd Number:"))
num3 = float(input("Enter the 3rd Number:"))

add_result = (num1 + num2 + num3)
print(add_result)  # o/p -> 10

mul_result = (num1 * num2 * num3)
print(mul_result)  # o/p -> 30

div_result = (num1 / num2) / num3
print(div_result)  # o/p -> 0.833334

sub_result = (num1 - num2 - num3)
print(sub_result)  # o/p -> 0.0
