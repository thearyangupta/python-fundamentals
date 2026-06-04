"""
Create a dict representing a student with: name, age, college, and a nested dict of marks (3 subjects:
math, english, cs). Then:
1. Print the student's name and age
2. Print only the math marks
3. Add a new subject (science) with a score
4. Update the english marks
5. Loop through all subjects and print "subject: marks" for each one
"""
student = {
    "name" : "Aryan gupta",
    "age" : "21",
    "college" : "xyz",
    "marks" : {
        "maths"  :99,
        "english" : 95,
        "cs" : 83
    }

}

print(student["name"],student["age"])
print(student["marks"]["maths"])
student["marks"]["science"] = 80
student["marks"]["english"] = 96
for subject, marks in student["marks"].items():
    print(subject + ":", marks)
