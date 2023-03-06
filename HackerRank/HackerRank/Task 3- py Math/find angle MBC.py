'''
Your task is to find angle MBC in degrees.

'''

import math

a=int(input())
b=int(input())

AB = math.sqrt(a**2 + 2*a*b)
MBC = math.atan(a/b) * 180/math.pi
MBC= round(MBC)
print(MBC, end=''), print("\u00b0")
