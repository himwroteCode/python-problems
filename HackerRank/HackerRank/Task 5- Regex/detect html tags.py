'''
Your task is to detect and print all the HTML tags, attributes and attribute values.

Print the detected items in the following format:

Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]


The -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value.
The > symbol acts as a separator of attributes and attribute values.

If an HTML tag has no attribute then simply print the name of the tag.
'''
from html.parser import HTMLParser

class HTMLTagParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))

n = int(input())
html_code = ""
for i in range(n):
    html_code += input().rstrip()

parser = HTMLTagParser()
parser.feed(html_code)
