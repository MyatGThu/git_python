#loops and dictionaries
# list() / x.value() / x.items()

#counting pattern

bbb = {'chuck'  : 100, 'fred': 32, 'jan' : 1002}

for xxx,ccc in bbb.items():
    print(xxx,ccc)


name = input('Enter file name: ')
handle = open(name)

counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
