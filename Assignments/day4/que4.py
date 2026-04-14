'''
Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km

---

'''
speed , time = map(int,input("enter speed & time: ").split())
print(f"Total time = {time} hours\nDistance = {speed*time} km")
