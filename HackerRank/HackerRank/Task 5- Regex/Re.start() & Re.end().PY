'''
You are given a string S.
Your task is to find the indices of the start and end of string K in S.
'''

import re
strg,k = input(),input()
ptrn = re.compile(k)
ver=ptrn.search(strg)

if not ver:
        print((-1,-1))  
while ver:
    print((ver.start(),ver.end()-1))
    ver=ptrn.search(strg,ver.start()+1)