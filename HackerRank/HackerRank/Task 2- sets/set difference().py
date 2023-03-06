'''
Task
Students of District College have a subscription to English and French newspapers.
Some students have subscribed to only the English newspaper,some have subscribed to
only the French newspaper, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper,
and one set has subscribed to the French newspaper. Your task is to find the total number of students
who have subscribed to only English newspapers.
 '''

n1=input()
li1 = input().split()
s1 = set(li1)
n2=input()
li2 = input().split()
s2 = set(li2)
s1s2 = s1.difference(s2)
print(len(s1s2))