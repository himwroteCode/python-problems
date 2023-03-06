'''
Task

You are given an HTML code snippet of N lines.
Your task is to print the single-line comments, multi-line comments and the data.

Print the result in the following format:

>>> Single-line Comment  
Comment
>>> Data                 
My Data
>>> Multi-line Comment  
Comment_multiline[0]
Comment_multiline[1]
>>> Data
My Data
>>> Single-line Comment:  
Note: Do not print data if data == '\n'.

'''
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
    
    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)

n = int(input())
html_code = ""
for _ in range(n):
    html_code += input().rstrip() + '\n'

parser = MyHTMLParser()
parser.feed(html_code)
