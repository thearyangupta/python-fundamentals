"""Take the 6 errors from Exercise 1. Wrap each in a try/except block so that instead of crashing, the
program prints a friendly message like "Oops: the key 'xyz' doesn't exist, please check."
Use specific exception types, not a bare except:. A bare except will haunt you in debugging for
years"""


# 1. NameError
try:
    print(does_not_exist)
except NameError:
    print("Oops: that variable doesn't exist, please define it first.")

# 2. TypeError
try:
    result = "hello" + 5
except TypeError:
    print("Oops: you tried to add a string and an int, which is not allowed.")

# 3. KeyError
my_dict = {"a": 1}
try:
    print(my_dict["b"])
except KeyError as e:
    print(f"Oops: the key '{e.args[0]}' doesn't exist, please check.")

# 4. IndexError
my_list = [1, 2, 3]
try:
    print(my_list[100])
except IndexError:
    print("Oops: that list index is out of range.")

# 5. ZeroDivisionError
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Oops: division by zero is not possible.")

# 6. FileNotFoundError
try:
    with open("no_such_file.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("Oops: the file doesn't exist, please check the filename.")
