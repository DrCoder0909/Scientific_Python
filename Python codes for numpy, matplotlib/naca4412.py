fname = open("ansys-4412.txt")
new= []
for line in fname:
    new1= line.replace("," , " ")
    new.append(new1)

for i, j in enumerate(new):
    print(1,i,j,2)
