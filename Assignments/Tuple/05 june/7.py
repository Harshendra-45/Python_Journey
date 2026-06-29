'''7. A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.
Tuple Format:
(player_id, player_name, runs_scored)
Requirements:
Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.
Test Case:
Input:
Enter number of players: 5
101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)
Highest Scorer:
(103, 'Gill', 120)
Lowest Scorer:
(104, 'Hardik', 38)
Total Runs:
361
Average Runs:
72.2
Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)
'''
n = int(input("Enter no of products: "))
players = []
for i in range(n):
    id = input("Enter product id: ")
    name = input("Enter product name: ")
    runs = int(input("Enter runs scored: "))
    players.append(tuple([id,name,runs]))

for i in players:
    print(i)

highest = players[0]
for i in players:
    if i[2]>highest[2]:
        highest=i
print("Highest scorer", highest)
low = players[0]
for i in players:
    if i[2]<low[2]:
        low=i
print("lowest scorer", low)

total = 0
for z in players:
    total+=z[2]
print("Total runs",total)
print("Average",total/n)

for d in players:
    if d[2]>50:
        print(d)