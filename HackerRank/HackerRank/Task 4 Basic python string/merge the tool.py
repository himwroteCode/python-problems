''' 

MEREGE THE TOOL problem of hackerrank in strings section


''' 


def merge_the_tools(string, k):
    substrings = [string[i:i+k] for i in range(0, len(string), k)]
    
    for substring in substrings:
        new_string = ''
        for char in substring:
            if char not in new_string:
                new_string += char
        print(new_string)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)