''' 
TASK
You are given a set A and N number of other sets. These N number of sets have to perform
some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.


'''


n = input()
s = set(map(int, input().split())) 

for _ in range(int(input())):
    args = input().strip().split()
    nw= set(map(int, input().split())) 
    eval("s." + args[0] + "(  nw  )")
print(sum(s))