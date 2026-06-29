doctors=[]
def adddoc():
            d = {}       
            d["pid"]=int(input("Enter id :"))
            d["name"]=(input("Enter name :"))
            d["specoalization"]=(input("Enter specialization :"))
            d["experience"]=int(input("Enter years of exp. :"))
            d["fees"]=float(input("Enter fees :"))
            doctors.append(d)
            
def showdoc():
            for i in doctors:
                print(i)
