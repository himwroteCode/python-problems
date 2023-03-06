'''
TASK

You are given some input, and you are required to check whether they are valid mobile numbers.

A valid mobile number is a ten digit number starting with a 7,8 or 9.

You are given a text of N lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:
'''

import re

pattern = re.compile(r'^[789]\d{9}$')

n = int(input())
strings = []
for i in range(n):
    strings.append(input())

for s in strings:
    if pattern.match(s):
        print('YES')
    else:
        print('NO')
