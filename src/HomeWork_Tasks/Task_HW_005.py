"""
**You want to check whether a web page loads within 3 seconds (performance test condition).
**
load_time = 4.2
⚠️ Page load too slow: 4.2 seconds

"""
# Step 1: Building logic
# i/p: load time = 4.2
# o/p: ⚠️ Page load too slow: 4.2 seconds

# Step 2: Rough Logic
# User Input function with float datatype
# if == load_time = 4.2 -> Page load too slow: 4.2 seconds ; else-> elif -> load time 0 and < = 3.0 -> Page loads within 3 secs ;
# elif >= 3.1 and 4.1 -> Page load is little slow

load_time = float(input("Enter the page load time: "))

if load_time == 4.2:
    print("⚠️ Page load too slow: 4.2 seconds")
else:
    if load_time <= 3.0:
        print("Page loads within 0-3 secs")
    elif load_time >= 3.1 and load_time <= 4.1:
        print("Page load is little slow")
    else:
        print("Invalid load time")
