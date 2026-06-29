'''Rotate characters by 3 positions to the right. '''
'''Rotate characters by n positions to the right.'''

s = input("Enter a string: ")
n = int(input("Enter rotation no: "))

if s == "":
    res = ""
else:
    rot = n % len(s)

    split = len(s) - rot

    res = s[split:] + s[:split]

print(res)