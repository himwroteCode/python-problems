'''
TASK:-

You are given a string S.
Your task is to find the first occurrence of an alphanumeric character in S.
(read from left to right) that has consecutive repetitions

'''
import re
st = input()

match = re.search(r"([a-zA-Z0-9])\1+", st)

if match:
    print(match.group(1))
else:
    print(-1)