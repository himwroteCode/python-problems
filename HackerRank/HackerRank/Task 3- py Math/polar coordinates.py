'''You are given a complex number Z. Your task is to convert it to polar coordinates.
'''

import cmath
c=complex(input())
a = c.real
b = c.imag
print(math.sqrt(a**2+b**2))
print(cmath.phase(complex(a,b)))