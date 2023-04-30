import matplotlib.pyplot as plt

years = range(2000, 2010)
divorce_rate = [5.0, 4.7, 4.6, 4.4, 4.3, 4.1, 4.2, 4.2, 4.2, 4.1]
margarine_consumption = [8.2, 7, 6.5, 5.3, 5.2, 4, 4.6, 4.5, 4.2, 3.7]

line1 = plt.plot(years, divorce_rate, "b-o",
                 label="Divorce rate in Maine")
plt.ylabel("Divorce per 1000 people")
plt.legend()

plt.twinx()
line2 = plt.plot(years, margarine_consumption, "r-o",
                 label="margarine consumption")
plt.ylabel(" lb of margarine(per capita)")

lines = line1+line2
labels = []
for line in lines:
    labels.append(line.get_label())

plt.legend(lines, labels)
plt.show()
