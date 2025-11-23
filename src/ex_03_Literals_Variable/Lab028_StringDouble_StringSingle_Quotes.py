c = 'C'
c1 = "C"

print(c)  # o/p ->  C
print(c1)  # o/p ->  C

dir = 'c:\Sachin\n.txt'
print(dir)  # o/p: c:\Sachin
# .txt

# To ignore \n from the text, we should use r - raw

dir = r'c:\Sachin\n.txt'  # r -> raw -> it will print as it by ignoring the escape seq
print(dir)

file_path = r"D:\Sachin_Personal\TheTestingAcademy\PythonCode\PyATB6xLearning\src\ex_03_Literals_Variable\Lab028_StringDouble_StringSingle_Quotes.py"
print(file_path)
