"""
**Check if the user can log in based on correct username and password.**
I/p
```
username = "admin"
password = "1234"
```
O/p
✅ Login Successful
For the Fail condition Other O/P = ❌ Invalid Credentials
"""

# Step 1: Building Logic
# i/p: username = "admin"
# i/p: password = "1234"
# o/p:Login Successful
# For the Fail condition Other O/P = ❌ Invalid Credentials

# Step 2: Rough Logic
# Use 2 input function - 1. Username and password -> username input should be in str and password field in int.
# if username ==admin and password == 1234 -> print login succesful ; else -> Invalid Credentials

username = str(input("Enter the username: ").lower().strip())
password = int(input("Enter the password: "))

if username == "admin" and password == 1234:
    print("✅ Login Successful")
else:
    print("❌ Invalid Credentials")
