'''
TASK 

Given N pairs of names and email addresses as input,
print each name and email address pair having a valid email address on a new line.

The first line contains a single integer, N, denoting the number of email address.
Each line i of the N subsequent lines contains a name and an email address as two space-separated values
following this format:
name <user@email.com>


'''
import re

for _ in range(int(input())):
    string = input()
    if re.search(r'<[a-zA-Z][\w\-.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>', string):
        print(string)
        