import re
summation=[]
hw=open("regexp.txt")
for line in hw:
    y=re.findall("[0-9]+",line)
    summation=summation+y
for i in range(0,len(summation)):
    summation[i]=int(summation[i])
print(sum(summation))

import re
print(sum([]))
