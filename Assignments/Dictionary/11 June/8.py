'''8.

=========================================
LIBRARY BOOK ISSUE TRACKER
==========================

A library records issued books.

books = [
"Python",
"Java",
"Python",
"C++",
"Java",
"Python"
]

Write a program to:

* Count how many times each book was issued.

Sample Output:
{
'Python':3,
'Java':2,
'C++':1
}

---
'''
books = [
"Python",
"Java",
"Python",
"C++",
"Java",
"Python"
]
issued ={}
for i in books:
    c = books.count(i)
    if i not in issued:
        issued[i] =c
print(issued)