largest=None
smallest=None
while True:
    int1= intput("please enter a positive integer number")
    if int1== "done":
        break
    try:
        int1=int(int)
    except:
        continue
    if int1>largest:
        largest=int1
    if int1<smallest:
        smallest=int1
print("AFTER", largest,smallest)
