#dictionaries chapter exercise


fname = input('Enter File: ')
if len(fname) < 1: fname = 'clown.txt'
handle = open(fname)

d = dict()

for line in handle:
    line = line.rstrip()
    # print(line)
    wds = line.split()
    # print(wds)
    for w in wds:
        print('**', w, d.get(w,-99))
        if w in d:
            d[w] = d[w] + 1
        else:
            d[w] = 1
        # print(w, d[w])

print(d)
