smallest= None
for value in [9,4,12,41,56]:
    if smallest is None:
        smallest= value
    elif value<smallest:
        smallest= value
    print(smallest, value)

print("After", smallest)
