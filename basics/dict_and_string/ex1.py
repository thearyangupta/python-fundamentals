"""Write a script that takes a full name (e.g., "prashant kumar sharma"), and prints:
1. the first name only
2. the last name only
3. the initials (P.K.S.)
4. the full name in Title Case
5. the full name reversed as a string
"""

name = "aryan gupta" 
parts=name.split()
first_name=parts[0]
last_name=parts[1]
print("first name:",first_name)
print("last name:",last_name)
intials=parts[0][0] +parts[1][0]
print("intials:",intials)
title_name=name.title()
print("title_name:",title_name)
reversed_name=name[::-1]
print("reversed_name:",reversed_name)
