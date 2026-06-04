"""
Write a function get_integer_input(prompt) that asks the user for a number and keeps asking
until they give a valid integer. If they enter "abc", it says "Not a number, try again" and asks again
"""

def get_integer_integer(prompt):
    while True:
        try:
            value =int(input("enter a number"))
            return value
        except ValueError:
            print("not a number try again")


num = get_integer_integer("enter a number")
print("you entered:",num)