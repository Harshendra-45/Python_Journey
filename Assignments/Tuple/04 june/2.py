''' 2.
Secure Password Analysis
A cybersecurity team wants to identify pairs of passwords having no common characters.
Problem Statement:
Given N strings, count the number of pairs that do not share any common character.
Example:
Input
N = 4
passwords[] = {"abc", "de", "fg", "ad"}
Output
3
Explanation
("abc","de")
("abc","fg")
("de","fg")
'''
n = int(input("Enter no of passwords: "))
pwd = tuple(map(str,input("Enter passwords: ").split(maxsplit=n)))
for i in range()