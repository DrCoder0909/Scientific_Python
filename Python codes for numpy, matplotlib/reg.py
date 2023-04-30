import re

hand=open("subtitle.txt")
for line in hand:
    if re.search("^Now", line):
        print(line)
