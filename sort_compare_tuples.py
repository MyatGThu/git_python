
d = {'a':10,'b':1,'c':22}
t = sorted(d.items())
print(t)

for k,v in sorted(d.items()):
    print(k,v)


#searching by values
print('\n')
c = {'a': 10,'b':1,'c':22}
tmp = list()

for k,v in c.items():
    tmp.append( (v,k) )
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)

#find words
print('\n')

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) +1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)

#shorter version
print('\n')

c = {'a': 10, 'b':1, 'c':22}

print(sorted ([ (v,k) for k,v in c.items() ] ) )
