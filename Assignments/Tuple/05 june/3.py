'''QUESTION 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

---

2. Display all patient details.

---

3. Display patients whose age is above 60 years.

---

4. Search for a patient using Patient ID.

---

5. Count the number of patients suffering from a particular disease.

---

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2'''
from collections import namedtuple
patient = namedtuple("patient",["id","name","age","disease"])
n = int(input("Enter a no:"))
p_list = []
for i in range(n):
    id = (input("Enter id: "))
    name = (input("Enter name: "))
    age = int(input("Enter age: "))
    dis = input("Enter disease: ")
    p_list.append(patient(id,name,age,dis))

for i in p_list:
    print(i)
print("\nPatient above 60")
for i in p_list:
    if i.age>60:
        print(i)

pid = input("enter patient id ")
for i in p_list:
    if i.id==pid:
        print("Patient found")
        print(i)

c = 0
dise = input("Enter disease to found: ")
for i in p_list:
    if i.disease==dise:
        c+=1
print("Patients with",dise)
print(c)