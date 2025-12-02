"""
    **In automation, you often compare expected and actual outputs.
        Write code to check if a test case passed or failed.**

expected_title = "Dashboard"
actual_title = "Dashboard "

✅ Test Passed – Title matches

True - why > Strip and convert them into the lowercase = both of them are equal.

"""
# Step 1: Building logic
# i/p: expected_title = "Dashboard"
# I/P: actual_title = "Dashboard "
# O/P: ✅ Test Passed – Title matches

# Step 2: Rough Logic:
# User input function in str datatype.
# if and else condition

expected_title = str(input("Enter the excepted title value: "))
actual_title = str(input("Enter the actual title value: "))

if expected_title.lower() == actual_title.lower().strip():
    print("✅ Test Passed – Title matches")
else:
    print("Test Failed -  Title did not match")
