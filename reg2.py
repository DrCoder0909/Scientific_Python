#this software uses regular expression for finding certain strings and objects
import re
x=" My least 2 3e favorite number is 19 and 39"
y= re.findall("[0-9]+",x)
print(y)
