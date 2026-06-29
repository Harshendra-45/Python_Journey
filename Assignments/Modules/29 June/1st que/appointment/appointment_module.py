app = []

def book_appointment():
            ap={}
            ap["app_id"]=int(input("Enter appointment id"))
            ap["p_id"]=int(input("Enter patient id"))
            ap["doc_id"]=int(input("Enter doctor id"))
            ap["app_date"]=(input("Enter appointment date "))
            ap["app_time"]=(input("Enter appointment time"))
            app.append(ap)
def show():
            for i in app:
                print(i)

