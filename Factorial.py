z=int(input("How many chances: "))
while z>0:
    n= int(input("int: "))
    for i in range (1,n):
        n=n*i
    z=z-1
    print(n)
