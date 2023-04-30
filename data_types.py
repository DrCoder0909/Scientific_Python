fhandle= open('hello.txt')
print(fhandle)
count=0
for line in fhandle:
    line=line.rstrip()
    print(line)
    count=count+1
print("Line count:", count)

fhand=open('hello.txt')
inp= fhand.read()
print(len(inp))
print(inp[:20])
