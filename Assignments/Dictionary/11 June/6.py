'''6.

=========================================
MOBILE APP DOWNLOAD COUNTER
===========================

Downloads received from different cities:

cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

Write a program to:

* Count downloads city-wise.
* Display city with maximum downloads.

Sample Output:
{'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
Most Downloads : Indore

---'''
cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]
dc = {}
for i in cities:
    v = cities.count(i)
    if i not in dc:
        dc[i]=v
print(dc)