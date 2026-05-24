""" Exercise 3 — nested loop, list of dicts 
 Create a list of 3 student dicts (each with name, marks_dict). Write a loop that prints each student's
 name, then a nested loop that prints each subject and mark indented beneath it. This is the exact
 pattern for displaying search results in a RAG system."""

students=[
    {"name": "Prashant", "marks_dict": {"math": 90, "english": 85}},
    {"name": "Pawan", "marks_dict": {"math": 75, "english": 80}},
    {"name": "Dheeraj", "marks_dict": {"math": 60, "english": 70}}
]
for student in students:
    print(student["name"])
    for subject, mark in student["marks_dict"].items():
        print(f"  {subject}: {mark}")