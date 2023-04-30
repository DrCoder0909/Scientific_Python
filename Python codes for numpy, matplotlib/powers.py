f = open("powers.txt", "w")
for i in range(1, 1001):
    print(i, i**2, i**3, i**4, sep=",", file=f)
f.close()
