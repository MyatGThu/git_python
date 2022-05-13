#slicing lists

t = [1,2,3,4,5,6,7,8,9,10]
print(t[1:3])
print(t[:4])

#list methods [appent , count, extend, index, insert, pop, remove, reverse, sort]


stuff = list()
stuff.append('book')

stuff.append(99)

stuff.append('cookie')

print(stuff)


some = [1,9,21,10,16]
y = 9 in some

print(y)

friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)


print(sum(some)/len(some))


numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' :break
    value = float(inp)
    numlist.append(value)
    
average = sum(numlist) / len(numlist)
print('Average: ', average)
