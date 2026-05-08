'''
8. Weather Monitoring System

A weather monitoring system classifies the weather condition based on temperature:

* Below 0°C → Freezing
* 0°C to 20°C → Cold
* 21°C to 35°C → Warm
* Above 35°C → Hot

Write a Python program to classify the weather.

Input:
Enter temperature: 38

Output:
Weather Condition: Hot
'''
temp = int(input("enter temperature: "))
if temp<0:
    print("Weather Condition: Freezing")
elif 0<temp<20:
    print("Weather Condition: Cold")
elif 21<temp<35:
    print("Weather Condition: Warm")
else:
    print("Weather Condition: Hot")