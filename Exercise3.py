total=0.0
count=0
while True:
    num= input("Enter number: ")
    if num=="done":
        print(count, total, total/count)
        break
    else:
        try:num=float(num)
        except:
            print("Invalid input")
            continue
        total= total+num
        count=count+1
