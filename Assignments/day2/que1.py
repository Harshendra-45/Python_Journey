'''
=====================================
Assignment 1: Time Converter
========================================

An event management company is developing a scheduling system. One of the key tasks is converting the duration of events from total seconds (which their sensor system records) into a more human-readable format of hours, minutes, and seconds.

Write a Python program that:
- Accepts the total event duration in seconds as input.
- Calculates how many hours, minutes, and seconds it corresponds to.
- Displays the output in the format:
  Hours: x, Minutes: y, Seconds: z

Sample Input:
Total event duration in seconds: 3672

Sample Output:
Hours: 1, Minutes: 1, Seconds: 12
''' 

total_sec = int(input("Enter total duration in second: "))
hours = total_sec//3600
minutes = (total_sec-(hours*3600))//60
sec = ((total_sec-hours*3600)-minutes*60)
print(hours,minutes,sec)

