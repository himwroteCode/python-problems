'''
Task
Students of District College have subscriptions to English and French newspapers.
Some students have subscribed to English only, some have subscribed to French only,
and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, 
and one set has subscribed to the French newspaper. Your task is to find the total number of students
who have subscribed to either the English or the French newspaper but not both.

 '''

n1=input()
li1 = input().split()
s1 = set(li1)
n2=input()
li2 = input().split()
s2 = set(li2)
s1s2 = s1.symmetric_difference(s2)
print(len(s1s2))
