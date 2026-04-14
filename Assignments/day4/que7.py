'''
Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67
'''
truns,overs = map(float,input("enter values : ").split())
ball = (int(overs)*6) + ((overs*10)%10)
runrate = truns / (ball/6)
print(f"Total balls = {ball}\nRun Rate = {runrate}")

