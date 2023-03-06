''' 
Task
You have a non-empty set s, and you have to execute N commands given in N lines.

The commands will be pop, remove and discard.

'''


#set.discard, .pop() & .remove()
n = int(input())
s = set(map(int, input().split()))
operations = int(input())

for x in range(operations):
  oper = input().split()
  if oper[0] == "remove":
    s.remove(int(oper[1]))
  elif oper[0] == "discard":
    s.discard(int(oper[1]))
  else:
    s.pop()
    
print(sum(s))
