"""
Program to demonstrate the type of the data type
"""

value = input("Enter the value of:")
print(value)
print(type(value))

# String (A bunch of char)

name = "Sachin"

c = 'C'
c1 = "C"

print(name)
print(type(name))
print(type(c))  # <class 'str'>
print(type(c1))  # <class 'str'>

print(len(name))  # 6
print(name.upper())  # SACHIN
print(name.lower())  # sachin
