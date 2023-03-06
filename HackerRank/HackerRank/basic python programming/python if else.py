n= int(input())

if n%2==1: #If  is odd, print Weird
    print('Weird')

if (n%2==0) and (2<=n<=5):  #If  is even and in the inclusive range of 2 to 5, print Not Weird
    print('Not Weird')

if (n%2==0) and 6<=n<=20:  #If  is even and in the inclusive range of 6 to 20, print Weird
    print("Weird")

if n%2==0 and n>20:  #If  is even and greater than 20 , print Not Weird
    print("Not Weird")