"""
You receive an API response code from your test script.
Write an if-else block to check whether the response is successful (status code 200) or not

```
I/P response = 404 , O/P ❌ Failed API Request
I/P response = 200 , O/P ✅ Passed API Request
```
"""

# Step 1: Building logic
# I/P response = 404 , O/P ❌ Failed API Request
# I/P response = 200 , O/P ✅ Passed API Request

# Step 2: Rough Logic
# User input function in float datatype
# if api_response == 200


api_response = float(input("Enter the api response code received: ").strip())

if api_response == 200:
    print("✅ Passed API Request")
else:
    if api_response == 404:
        print("❌ Failed API Request")
    elif api_response <= -1 or api_response < 200:
        print("Not valid response code")
    elif api_response >= 201 and api_response < 404:
        print("Not valid range between 201 to 404")
    else:
        print("Out of range, Please check the response code")
