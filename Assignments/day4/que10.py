'''
Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4
'''
totalsec = int(input("enter total sec : "))
hrs = totalsec//3600
min = (totalsec-hrs*3600)//60
sec = (totalsec-hrs*3600-min*60)
print(F"Hours = {hrs}\nMinutes = {min}\nSeconds = {sec}")

