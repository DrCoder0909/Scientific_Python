count=0
sum=0
print("Before", count,sum)
for value in [12,23,34,45,56,67,78,445,56,6,76,7,65,65,667,6,78]:
    count=count+1
    sum=sum+value
    print(count, sum, value)
print("After", count, sum, sum/count)
