# dictionaries common applications
# in operator to look up in dictionaries


#histogram code

counts = dict()
names = ['csev', 'cwen', 'csev', 'rqian', 'cwen', 'cwen']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts.get(name,0) + 1
print(counts)

#get method for dictionaries
#if name in counts:
#    x = counts[name]
#else:
#    x = 0

# x = counts.get(name,0)
