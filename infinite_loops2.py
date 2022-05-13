largest_so_far = -2

print('Before: ', largest_so_far)

for new_num in [9, 41, 12, 3, 74, 15]:
    if largest_so_far < new_num:
        largest_so_far = new_num
    print(largest_so_far, new_num)

print('After: ', largest_so_far)
