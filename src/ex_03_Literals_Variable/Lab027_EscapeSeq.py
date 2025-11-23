"""
Program to demonstrate the Escape Sequence

"""
"""
\n -> Print the output in the new line
\t -> Print the output with 4 spaces
\b -> Deletes the one word seq
"""

print("Sachin\nKulambi")  # o/p: Sachin
#  Kulambi
print("Sachin\tKulambi")  # o/p -> Sachin	Kulambi
print("Sachin\bKulambi")  # o/p -> SachiKulambi
print("Sachin\\Kulambi")  # o/p -> Sachin\Kulambi
print("Sachin\'Kulambi")  # o/p -> Sachin'Kulambi
print("Sachin\"Kulambi")  # o/p -> Sachin"Kulambi
print("Sachin\rKulambi")  # 0/p -> Kulambi (The \r escape character moves the cursor to the beginning of the line. It can overwrite the existing text.)
print("Sachin\fKulambi")  # o/p -> SachinKulambi (Form Feed – Moves the cursor to the next page.)
print("Sachin\vKulambi")  # o/p -> SachinKulambi (Vertical Tab – Moves the cursor vertically.)
print("Sachin\x48Kulambi") # o/p -> SachinHKulambi (\x48 -> is hexadecimal value of character 'H')
