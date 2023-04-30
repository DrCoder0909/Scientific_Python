import sys
import os

months= ["jan", "feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]

dir_name= sys.argv[1]
for filename in os.listdir(dir_name):
    #filename is expected to be in the form of "data -DD- MMM-YY.txt"
    d, month,y= int(filename[5:7]),filename[8:11], int(filename[12:14])
    m=months.index(month.lower())+1

    newname= "data-20{:02d}-{:02d}-{:02d}.txt".format(y,m,d)
    newpath=os.path.join(dir_name,newname)
    oldpath=os.path.join(dir_name, filename)
    print(oldpath,"-->", newpath)
    os.rename(oldpath,newpath)
