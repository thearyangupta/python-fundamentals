"""
Write a function (you'll learn the def syntax tomorrow — for now just use a variable) that takes a marks
value (0–100) and prints:
A+ (≥90), A (80–89), B (70–79), C (60–69), D (50–59), Fail (<50).
Handle invalid input: if marks < 0 or > 100, print "Invalid input".
"""

a= int(input("enter your marks"))
print("your marks is:",a)

if(a <0 or a>100):
    print("invalid")
elif(a>=90):
    print("A+")
elif(a>=80):
    print("A")
elif(a>=70):
    print("B")
elif(a>=60):
    print("C")
elif(a>=50):
    print("D")
else:
    print("fail")


print("good luck")