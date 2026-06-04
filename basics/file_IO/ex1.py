"""Create a file notes.txt manually with 5 lines of text. Write a Python script that:
1. Reads the file and prints each line with a line number
2. Writes a new file notes_upper.txt with all text in uppercase
3. Writes a new file notes_count.txt containing only the word count"""
"""
1st part

f = open("notes.txt","r")
lines = f.readlines()
for i,line in enumerate(lines,start=1):
    print(f"line{i}:{line.strip()}")"""

"""
2nd part

with open("notes_upper.txt","w") as f:
    with open("notes.txt","r") as f_read:
        lines=f_read.readlines()
        for line in lines:
            f.write(line.upper())"""
"""
3rd part

with open("notes_count.txt","w") as f:
    with open("notes.txt","r") as f_read:
        lines=f_read.read()
        word_count = len(lines.split())
        f.write(f"word count:{word_count}")
    """    