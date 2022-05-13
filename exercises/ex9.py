#dictionaries chapter exercise


fname = input('Enter File: ')
if len(fname) < 1: fname = 'clown.txt'
handle = open(fname)

d = dict()

for line in handle:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        #idiom retrieve/create/update counter
        d[w] = d.get(w,0) + 1
        print(w, 'new', d[w])
# print(d)

#find the most common word in the dict

largest = -1

for x,y in d.items(): #x and y = key and value inside dict()
    print(x,y)
    if y > largest:
        largest = y
        theword = x #capture the largest key

print('Done', largest, theword)
