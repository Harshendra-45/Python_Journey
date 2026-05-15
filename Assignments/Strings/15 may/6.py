'''
6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number'''
pnr = input("Enter the PNR: ").upper()
s =""
valid = 0
count=0
if len(pnr)==12:

    i = 0
    for ch in pnr:
        while i<=2:
            s+=pnr[i]
            i+=1
        if ch.isdigit():
            count += 1
        
    print(s)
    print(count)
    if count==len(pnr)-3 and s=="PNR":
        valid=1
    print("Valid PNR Number") if valid==1 else print("Invalid")
            
'''
optimized code using slicing
pnr = input("Enter PNR: ").upper()

if len(pnr) == 12 and pnr[:3] == "PNR" and pnr[3:].isdigit():
    print("Valid PNR Number")
else:
    print("Invalid")
'''