largest_so_far=-1
for value in [1,23,4,45,5,66,778,7,99,90,2324,34,5,4,657,687,9,23,3,46,576,87,898]:
    if value>largest_so_far:
        largest_so_far=value
print(largest_so_far)
smallest=largest_so_far
for value in [1,23,4,45,5,66,778,7,99,90,2324,34,5,4,657,687,9,23,3,46,576,87,898]:
    if value<smallest:
        smallest=value
print(smallest)
