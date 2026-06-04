"""
Ask the user to enter an age using input(). If they enter a non-number, print "Please enter a
number". If age is negative or > 150, print "Unrealistic age". Otherwise print age category (child / teen /
adult / senior). Hint: use .isdigit() to check if a string is a number"""

age =input("enter your age:")

if not age.isdigit():
    print("please enter a number")
else:
    age = int(age)
    if age<0 or age>150:
        print("unrealsitic age")
    elif age < 15:
        print("Child")
    elif age < 20:
        print("Teen")
    elif age < 40:
        print("Adult")
    else:
        print("Senior")