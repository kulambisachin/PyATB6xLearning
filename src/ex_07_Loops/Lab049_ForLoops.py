for i in range(0, 10, 2):
    print(i)                # o/p: 0,2,4,6,8

print("\n")

for i in range(0, 10, 3):
    print(i)                # o/p: 0,3,6,9

for i in range (0, 10, 1.5):
    print(i)                # o/p: TypeError: 'float' object cannot be interpreted as an integer
