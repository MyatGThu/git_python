#e.g. tuples: y = ()  list: y = []
# tuples cannot be altered after assigning value inside. "Immutable"

#corrorsponding tuples.
(x , y) = (4, 'Fred')
print(y)

(a , b) = (99, 98)
print(a)


#tuples & dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4

for (k,v) in d.items():
    print(k,v)

tups = d.items()
print(tups)

#Tuples are comparable
x = (0,1,2) < (5,1,2)
print(x)

y = ('Jones', 'Sally') > ('Jones', 'Sam')
print(y)

#Sorting Tuples
#next lesson
