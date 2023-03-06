'''
Task

You are given a text of N lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:

&& → and
|| → or
Both && and || should have a space " " on both sides.

'''

import re

number = int(input())
pattern_and_this = re.compile('(?<=[ ])[&]{2}(?=[ ])')
pattern_or_that = re.compile('(?<=[ ])[|]{2}(?=[ ])')
for _ in range(number):
    ln = input()
    
    ln = re.sub(pattern_and_this, 'and', ln)
    ln = re.sub(pattern_or_that, 'or', ln)
    
    print(line)
    