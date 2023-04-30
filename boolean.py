found= False
print("Before", found)
for value in [1,2,3,4,5,6,8,9,5,4,2,1,3,34.5,46]:
    if value==3:
        found=True
        break
    print(found,value)
print("After", value)
