tot=0.0
count=0
while True:
    sval=input("Enter number: ")
    if sval=="done":
        print(tot, count, tot/count)
        break
    try:fval=float(sval)
    except:
        print("Invalid Input")
        continue
    count=count+1
    tot=tot+fval
