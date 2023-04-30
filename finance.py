import datetime
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.dates import strpdate2num
from datetime import datetime

def date_to_int(s):
    epoch = datetime(year = 1970 , month =1 , day = 1)
    date= datetime.strptime(s, "%Y-%m-%d")
    return (date-epoch).days

def bindate_to_int(bs):
    return date_to_int(bs.decode("ascii"))

def reformat_lines(fi):
    for line in fi:
        print(type(line))
        for st in line:
            st[2]= "-"
            st[5]="-"
    return fi


with open("bp-share-prices.txt") as fi:
    dt = np.dtype([("daynum", "i8"), ("close", "f8")])
    share_price = np.genfromtxt(reformat_lines(fi), delimiter = " ",skip_header =1,
                                     usecols = (0,4),converters = {0:bindate_to_int}, dtype=dt)

fig ,ax= plt.subplots()
ax.plot(share_price["daynum"], share_price["close"], c = "g")
ax.fill_between(share_price["daynum"], 0 , share_price["close"], facecolor='g',
                alpha = 0.5)

daymin, daymax = share_price["daynum"].min(), share_price["daynum"].max()
ax.set_xlim(daymin, daymax)

price_max = np.max(share_price["close"])

def get_xy(date):
    """ return the (x,y) coordinates of the share price on a given date"""
    x = date_to_int(date)
    return share_price[np.where(share_price["daynum"]==x)][0]

x , y = get_xy("2021-12-08")
ax.annotate("share split", (x,y), xytext = (x+1000,y), va = "center",
            arrowprops= dict(facecolor="black", shrink = 0.05))
x, y = get_xy("2020-12-18")
ax.annotate("Deepwater Horizon\noil spill" , (x,y), xytext = (x, price_max*0.9),
             arrowprops = dict(facecolor = "black", shrink = .05), ha = "center")

plt.show()
