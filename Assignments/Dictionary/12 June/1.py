'''
1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.

The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:

Key → Patient ID
Value → Dictionary containing patient details

Each patient record should contain:

Patient Name
Age
Gender
Disease
Doctor Name
Sample Data Structure
{
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit

Functional Requirements
1. Add New Patient

Accept the following information from the user:

Patient ID
Patient Name
Age
Gender
Disease
Doctor Name

Store the record in the nested dictionary.

Validation:
If the Patient ID already exists, display:

Patient ID already exists.

2. Search Patient

Accept Patient ID from the user.

If the patient exists, display complete information.

Sample Output

Patient ID : 101
Name       : Ajay
Age        : 35
Gender     : Male
Disease    : Fever
Doctor     : Dr. Sharma

If Patient ID is not found:

Patient Record Not Found

3. Update Patient Disease

Accept Patient ID.

If found:

Ask for new disease.
Update the disease information.

Sample Output

Disease Updated Successfully
4. Delete Patient Record

Accept Patient ID.

If found:

Remove the patient record.

Sample Output

Patient Record Deleted Successfully

Otherwise:

Patient Not Found
5. Display All Patients

Display all patient records in a formatted manner.

Sample Output

--------------------------------
Patient ID : 101
Name       : Ajay
Age        : 35
Disease    : Fever
Doctor     : Dr. Sharma
--------------------------------

Patient ID : 102
Name       : Ravi
Age        : 42
Disease    : Diabetes
Doctor     : Dr. Gupta
6. Count Total Patients

Display the total number of patients currently stored.

Sample Output

Total Patients : 25
7. Display Patients By Disease

Accept a disease name from the user.

Display all patients suffering from that disease.

Sample Output

Enter Disease : Fever

101  Ajay
108  Aman
115  Neha

If no patient is found:

No Patient Found
8. Display Oldest Patient

Find and display the patient having the highest age.

Sample Output

Oldest Patient Details

Patient ID : 110
Name       : Ravi
Age        : 68
Disease    : Diabetes
Doctor     : Dr. Gupta
9. Display Youngest Patient

Find and display the patient having the minimum age.

Sample Output

Youngest Patient Details

Patient ID : 121
Name       : Riya
Age        : 4
Disease    : Viral Fever
Doctor     : Dr. Mehta
10. Exit

Terminate the application.

Sample Output

Thank You For Using Hospital Patient Management System
'''

hospital ={}
while True:
    print("=====================================\n\
    HOSPITAL PATIENT MANAGEMENT SYSTEM\n\
    =====================================\n\
    1. Add New Patient\n\
    2. Search Patient\n\
    3. Update Patient Disease\n\
    4. Delete Patient Record\n\
    5. Display All Patients\n\
    6. Count Total Patients\n\
    7. Display Patients By Disease\n\
    8. Display Oldest Patient\n\
    9. Display Youngest Patient\n\
    10. Exit")
    ch = int(input("Enter choice: "))
    match ch:
        case 1:
            patient_id = int(input("Enter patient id: "))
            if patient_id in hospital:
                print("Patient ID already exists.")
            else:
                hospital[patient_id]={}
                hospital[patient_id]["name"] =input("Enter name: ")
                hospital[patient_id]["age"] =int(input("Enter age: "))
                hospital[patient_id]["gender"] =input("Enter gender: ")
                hospital[patient_id]["disease"] =input("Enter disease: ")
                hospital[patient_id]["doc"] =input("Enter doctor  name: ")
        case 2:
            id = int(input("Enter patient id: "))
            for k,v in hospital.items():
                if k==id:
                    print("\nPatient id:",id)
                    for k,v in v.items():
                        print(k,":",v)

            if id not in hospital:
                print("Patient record not found")
        case 3:
            id = int(input("Enter patient id: "))
            if id in hospital:
                dis = input("Enter disease to update")
                hospital[id]["disease"]=dis
                print("Disease updated successfully")
            else:
                print("Patient not found")
        case 4:
            id = int(input("Enter patient id: "))
            if id in hospital:
                hospital.pop(id)
                print("Record deleted succesfully")
            else:
                print("Patient not found")
        case 5:
            for k,v in hospital.items():
                print(k)
                for k,v in v.items():
                    print("-------------------")
                    print(k,":",v)
        case 6:
            print("Total Patients",len(hospital))
        case 7:
            dis = input("Enter disease: ")
            for k,v in hospital.items():
                if hospital[k]["disease"] == dis:
                    print(k, hospital[k]["name"])
        case 8:
            for k,v in hospital.items():
                age = (list(hospital[k]["age"]))
                max(age)
        case 9:
            for k,v in hospital.items():
                for k,v in v.items():
                    z = (min(v["age"]))
                    if v==z:
                        print(k,":",v)
        case 10:
            print("Thank You For Using Hospital Patient Management System")
            break   
        case _:
            print("Invalid output")