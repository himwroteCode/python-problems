''' 
Task
The students of District College have subscriptions to English and French newspapers.
Some students have subscribed only to English, some have subscribed only to French,
and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper,
one set has subscribed to the French newspaper. Your task is to find the total number of students
who have subscribed to both newspapers.

'''

n1=input()
li1 = input().split()
s1 = set(li1)
n2=input()
li2 = input().split()
s2 = set(li2)
s1s2 = s1.intersection(s2)
print(len(s1s2))