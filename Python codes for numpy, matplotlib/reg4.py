import re
lin= "From stephen.marquard@uca.sc.ut St Jun 5 12:12:43 2009"
y= re.findall("@[^ ]*", lin)
print(y)
