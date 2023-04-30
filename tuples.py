fhand = open("subtitle.txt")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0)+1

first = list()
for key, val in counts.items():
    a = first.append((val, key))

first = sorted(first, reverse=True)

for val, key in first[:10]:
    print(key, val)
