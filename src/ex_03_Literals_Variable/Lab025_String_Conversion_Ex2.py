"""
Program to demonstrate the string contention

"""

name = "This is a big line text"

print(type(name))   # o/p -> <class 'str'>
name = name + str(1)
print(name)   # o/p -> This is a big line text1

first_name = "Sachin"
last_name = "Kulambi"

full_name = first_name + ' ' + last_name
print(full_name)  # o/p -> Sachin Kulambi
print(type(full_name)) # o/p -> <class 'str'>

name = name + 1  # o/p -> TypeError: can only concatenate str (not "int") to str
print(name)



