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

#print(d,'\n')


tmp = list()
for k,v in d.items():
    nt = (v,k)
    tmp.append(nt)
#print('Flipped',tmp,'\n')

tmp = sorted(tmp, reverse=True)
#print('Sorted',tmp[:5])

for v,k in tmp[:5]:
    print(k,v)
