"""
Write a program to calculate area of circle given radius using the formula
(area = pie*r^2) pie -> 3.14
"""
import math

# i/p: r -> float
# o/p: String formatted output of area.

# Step 1: Building the logic:

r = float(input("Input value of r is: "))
print(r)  # Printing where the output is displaying the float format

pie = 3.14  # Assigning the pie value
# area = pie * (r ** 2)  # Area of Circle formula
area = math.pi * pow(r, 3)
# area = pie * pow(r, 2)

print("Area of the circle is: ", area)

# String Formatting, Formatted string literals
print(f"Area of the the circle is {area:.1f}")  # To get the decimal value to 1 point (Data Formatting)
