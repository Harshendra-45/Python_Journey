'''QUESTION 5: LIBRARY BOOK RECORDS
================================
A library maintains book information using NamedTuple.
Fields:
book_id, title, author, price
Requirements:
1. Read N book records from the user and store them in a list of NamedTuples.
---
2. Display all book details.
---
3. Find and display the most expensive book.
---
4. Search books by author name.
---
5. Calculate and display the average price of all books.
---
Test Case:
Input:
Enter number of books: 4
B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300
Enter Author Name: John
Expected Output:
Most Expensive Book:
B103 Data Science John 700
Average Book Price:
500.0
Books Written By John:
B101 Python Basics John 450
B103 Data Science John 700
'''
from collections import namedtuple
library = namedtuple("library",["id","title","author","price"])
n = int(input("Enter a no:"))
llist = []
for i in range(n):
    id = (input("Enter  book id: "))
    name = (input("Enter title of book: "))
    pr_name = input("Enter author name: ")
    amount = int(input("Enter price: "))
    llist.append(library(id,name,pr_name,amount))

for i in llist:
    print(i)
max = llist[0]
for i in llist:
    if i.price>max.price:
        max=i
print("most expensive:",max)
atname = input("Enter author name:").lower()
for i in llist:
    if i.author.lower()==atname:
        print(i)
sales = 0
for i in llist:
    sales+=i.price
print("Average",sales/n)
