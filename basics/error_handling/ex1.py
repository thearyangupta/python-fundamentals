"""Intentionally cause each of these errors in a single file. For each, read the traceback and write a
one-line comment explaining what went wrong:
1. NameError — use a variable that doesn't exist
2. TypeError — add a string to an int
3. KeyError — access a dict key that doesn't exist
4. IndexError — access my_list[100] when the list has 3 items
5. ZeroDivisionError — divide by zero
6. FileNotFoundError — open a file that doesn't exist"""



# 1. NameError — variable not defined
print(does_not_exist)  
# NameError: 'does_not_exist' is not defined

# 2. TypeError — adding string to int
result = "hello" + 5  
# TypeError: cannot concatenate str and int

# 3. KeyError — dict key missing
my_dict = {"a": 1}
print(my_dict["b"])  
# KeyError: 'b' key not found in dictionary

# 4. IndexError — list index out of range
my_list = [1, 2, 3]
print(my_list[100])  
# IndexError: list index 100 out of range

# 5. ZeroDivisionError — division by zero
print(10 / 0)  
# ZeroDivisionError: division by zero is undefined

# 6. FileNotFoundError — file does not exist
with open("no_such_file.txt") as f:
    data = f.read()
# FileNotFoundError: 'no_such_file.txt' not found


