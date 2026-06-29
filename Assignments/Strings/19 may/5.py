'''
5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website
'''
web = input("Enter a string: ")
start =""
end=""
# print(len(web))
# print(len(web)-4)
# print(web[9])
for x in range(0,len(web)):
    if x<=3:
        start+=web[x]
        # print(start)
    elif x>=len(web)-4:
        end+=web[x]
# print(start)
# print(end)
if start=="www." and end==".com":
    print("Valid website")
else:
    print("Invalid url")