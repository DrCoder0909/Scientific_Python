import matplotlib.pyplot as plt
import numpy as np

text_file = "moby-dick.txt"

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lcount = dict([(letter,0) for letter in letters])

for letter in open(text_file).read():
    print(letter[6770])
    try:
        lcount[letter.upper()] +=1
    except KeyError:
        pass
norm = sum(lcount.values())

fig, ax = plt.subplots()
x = range(26)
ax.bar(x, [lcount[letter]/norm*100 for letter in letters], width= 0.8,
       color = 'g' , alpha = 0.5 , align ="center" )
ax.set_xticks(x)
ax.set_xticklabels(letters)
ax.tick_params(axis = "x" , direction = "out")
ax.set_xlim(-0.5, 25.5)
ax.yaxis.grid(True)
ax.set_ylabel("Letter Frequency, %")
plt.show()
