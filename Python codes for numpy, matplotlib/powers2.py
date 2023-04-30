f = open("powers.txt", "r")
sqaures, cubes, fourths = [], [], []
for line in f:
    fields = line.split(",")
    sqaures.append(fields[1])
    cubes.append(fields[2])
    fourths.append(fields[3])
f.close()
n = 500
print(n, "cube is ", cubes[n-1])
