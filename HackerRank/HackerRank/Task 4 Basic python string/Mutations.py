'''
Task
Read a given string, change the character
at a given index and then print the modified string.

'''
def mutate_string(string, position, character):
    string_list = list(string)
    
    string_list[position] = character
    
    new_string = "".join(string_list)
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)