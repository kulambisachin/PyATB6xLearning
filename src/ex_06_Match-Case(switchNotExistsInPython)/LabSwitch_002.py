"""
Write a program to demonstrate the match-case conditions

"""
# Step 1: Building logic
# i/p: API, UI, Performance Security Test case, Default value.
# o/p: Running the API, UI, Performance, Security Test case respectively.

# Step 2: Rough Logic
# User input with the str data type.
# match Test type with API, UI, Performance, Security

test_type = str(input("Enter the test type of execution: ").strip().lower())

match test_type:
    case "api":
        print("You are executing the api test case")
    case "ui":
        print("You are executing the ui test case")
    case "performance":
        print("You are executing the performance test case")
    case "security":
        print("You are executing the security test case")
    case _:
        print("Invalid Test Case input")

# Write a same above program with if and elif condition

test_type = str(input("Enter the test type of execution: ").strip().lower())

if test_type == "api":
    print("You are executing the api test case")
elif test_type == "ui":
    print("You are executing the ui test case")
elif test_type == "performance":
    print("You are executing the performance test case")
elif test_type == "security":
    print("You are executing the security test case")
else:
    print("Invalid Test Case input")
