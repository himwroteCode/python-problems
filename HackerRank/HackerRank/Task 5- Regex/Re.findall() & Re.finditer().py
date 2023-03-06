'''
TASK
You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of S that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only.

'''

import re
example_string = input()
the_exp = r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiou])'
matchings = re.findall(the_exp, example_string , flags=re.IGNORECASE)
if matchings:
    for match in matchings:
        print(match)
else:
    print(-1)
