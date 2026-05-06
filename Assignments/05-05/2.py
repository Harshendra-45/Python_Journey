# 2. University Result Processing System
# A university wants to automatically assign grades based on marks.
# Marks ≥90 → A+
# Marks ≥75 → A
# Marks ≥60 → B
# Marks ≥50 → C
# Below 50 → Fail
# Write a program using a single nested inline if expression to display the grade.

mrk=int(input("enter marks "))

grd="A+" if mrk>=90 else"A" if mrk>=75 else "B" if mrk>=60 else "C" if mrk>=50 else "fail"
print(grd)