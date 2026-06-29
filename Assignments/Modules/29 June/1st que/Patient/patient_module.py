Patient=[]
def add_patient():
    d = {}       
    d["pid"]=int(input("Enter id :"))
    d["name"]=(input("Enter name :"))
    d["age"]=int(input("Enter age :"))
    d["gender"]=(input("Enter gender :"))
    d["disease"]=(input("Enter disease :"))
    d["mob_no"]=int(input("Enter phone no :"))
    Patient.append(d)
                
def search_patient():
    p_id = int(input("Enter a id :"))
    for i in Patient:
                    if i["pid"]==p_id:
                        print("Found")
                        print(i)
                        break
    else:
                    print("Patient not found")

def display():
        for i in Patient:
                    print(i)
    
