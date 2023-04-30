#greedy regular expression
import re
x ="From: The greedy expression category: we display this"
y= re.findall("^F.+:", x)
print(y)
