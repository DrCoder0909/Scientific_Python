
numlist=list()
while True:
    inp= input("Enter a number: ")
    if inp=="done": break
    value=float(inp)
    numlist.append(value)

average= sum(numlist)/len(numlist)
print("Average:", average)

abc="With three words"
stuff=abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff:print(w)
