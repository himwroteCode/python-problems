
'''
RANGOLI problem in hackerrank under string section

 '''

def print_rangoli(size):
    # your code goes here
    centers = list(range(size - 1, 0, -1)) + list(range(0, size))
    for c in centers:
        digits = list(range(size - 1, c, -1)) + list(range(c, size))
        print('-'.join([chr(d + ord('a')) for d in digits]).center(4 * size - 3, '-'))