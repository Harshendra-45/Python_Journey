'''Assignment: Hospital Management System Using Python Packages and Modules
Problem Statement:
Develop a menu-driven Hospital Management System application in Python.
The application should be developed using proper packages and modules. 
Do not write the complete program in a single file. Divide the application
into different packages based on functionality.
Project Structure:
HospitalManagement/

    main.py

    patient/
        __init__.py
        patient_module.py

    doctor/
        __init__.py
        doctor_module.py

    appointment/
        __init__.py
        appointment_module.py

    billing/
        __init__.py
        billing_module.py
Requirements:
1. Patient Management Package
Create a package named "patient".
create module:
patient_module.py
Implement the following functions:
a) add_patient()
Take patient details from user:
- Patient ID
- Patient Name
- Age
- Gender
- Disease
- Mobile Number

Store patient information using list and dictionary.

b) display_patients()

Display all registered patients.

c) search_patient()
Search patient details using Patient ID.
--------------------------------------------------'''
from Patient import patient_module
from doctor import doc_management
from appointment import appointment_module
from billing import billing_module
while True:
    print("========== Hospital Management System ==========")
    print("1. Add Patient")
    print("2.Display Patients")
    print("3. Search Patient")
    print("4. Add Doctor")
    print("5. Display Doctors")
    print("6. Book Appointment")
    print("7. Show Appointments")
    print("8. Generate Bill")
    print("9. Exit")
    chx = int(input("Enter a choice: "))
    match chx:
        case 1:
            patient_module.add_patient()
        case 2:
            patient_module.display()
        case 3:
            patient_module.search_patient()
        case 4:
            doc_management.adddoc()
        case 5:
            doc_management.showdoc()
        case 6:
            appointment_module.book_appointment()
        case 7:
            appointment_module.show()
        case 8:
            billing_module.gen_bill()
        case 9:
            print("Exiting system")
            break
        case _:
            print("Invalid input")


