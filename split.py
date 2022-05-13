abc = 'with three words'
stuff = abc.split()

print(stuff)
print(len(stuff))

print(stuff[0])

for w in stuff:
    print(w)

line = 'first;second;thrid' #only remove white spaces i.e. tabs space etc
thing = line.split()

print(thing)

thing = line.split(';') #asking split to look for what to remove and add to list
print(thing)
