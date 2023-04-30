count = dict()
srt_list = list()

fhand = open(input("Enter the text doc here"))
for line in fhand:
    words = line.split()
    for word in words:
        count[word] = count.get("word", 0)+1

print(type(count.items()))
