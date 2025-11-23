"""
Task for the Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1

"""
from math import remainder

# Step 1: Building a logic

# i/p: num1, num2
# o/p: Quotient and Remainder

num1 = float(input("Enter a num1 value: "))
num2 = float(input("Enter the num 2 value: "))

result = (divmod(num1, num2))
print(result)

# Two method of displaying the output with the operations

quotient = num1 // num2
remainder = num1 % num2

print("The quotient value of 15/2 is =", quotient)
print("The remainder value of 15/2 is =", remainder)
