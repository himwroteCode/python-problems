''' 
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N*M. ( is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters


'''

N, M = map(int, input().split())

# Top design
for i in range(N // 2):
    print(('.|.' * (2*i + 1)).center(M, '-'))

# Welcome line
print('WELCOME'.center(M, '-'))

# Bottom design
for i in range(N // 2 - 1, -1, -1):
    print(('.|.' * (2*i + 1)).center(M, '-'))


