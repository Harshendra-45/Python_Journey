'''5.

=========================================
WORD LENGTH GROUPING
====================

A content management system stores article tags.

tags = ["python","java","api","react","html","css"]

Write a program to:

* Group words according to their length.
* Store result in dictionary.

Sample Output:
{
3:['api','css'],
4:['java','html'],
5:['react'],
6:['python']
}

---'''
tags = ["python","java","api","react","html","css"]
diction = {}
for i in tags:
    c = len(i)
    if c not in diction:
        diction[c]=[]
    diction[c].append(i)
print(diction)