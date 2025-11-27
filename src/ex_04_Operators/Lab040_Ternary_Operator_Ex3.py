"""
Program to demonstrate the one line ternary operator
"""

user_age = int(input("Enter the age of the user: "))

# if user_age >= 18:
#     print("He has voting rights")
# else:
#     print("He doesn't have voting rights")

print("He has voting rights" if user_age >= 18 else "He doesn't have voting rights")
