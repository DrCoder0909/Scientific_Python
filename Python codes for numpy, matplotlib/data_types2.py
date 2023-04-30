fname=input("Enter a file name: ")
try:
    fhandle=open(fname)
except:
    print("File cannot be opened: ", fname)
    quit()
count=0
for line in fhandle:
    if "i" in line:
        count=count+1
print("There were", count, "subject lines in", fname)
