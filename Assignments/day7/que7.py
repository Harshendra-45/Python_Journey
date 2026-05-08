'''
7. Banking Withdrawal Limit System


A bank wants to set withdrawal limits based on the available account balance:

* Balance less than ₹1000 → Withdrawal not allowed
* ₹1000 to ₹5000 → Maximum withdrawal ₹1000
* Above ₹5000 → Maximum withdrawal ₹5000

Write a Python program to display the withdrawal limit.

Input:
Enter account balance: 3500

Output:
Maximum Withdrawal Limit: ₹1000
'''
bal = int(input("Enter account balance: "))
if bal<1000:
    print("Withdrawal not allowed")
elif 1000<bal<5000:
    print("Maximum withdrawal ₹1000")
else:
    print("Maximum withdrawal ₹5000")