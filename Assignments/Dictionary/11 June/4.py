'''4.
=========================================
STUDENT GRADE ANALYSIS
======================
Store student marks in a dictionary.
students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65

---'''
students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

high = max(students.values())
low = min(students.values())
for k,v in students.items():
    if v == max:
        print("Highest marks",k,v)
    elif v==min:
        print("lowest marks",k,v)