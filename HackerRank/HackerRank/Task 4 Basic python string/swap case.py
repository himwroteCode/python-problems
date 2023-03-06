'''
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
'''
def swap_case(s):
    swapped = ""
    for char in s:
        if char.islower():
            swapped += char.upper()
        elif char.isupper():
            swapped += char.lower()
        else:
            swapped += char
    return swapped
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)