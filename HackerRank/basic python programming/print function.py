'''
Task

Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between
'''

n= int(input())
st = ''
for i in range(1,n+1):
    st2= str(i)
    st=st+st2

print(st)
