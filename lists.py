#lists are mutable

fruit = 'Banana'
#fruit[0] = 'b'

x = fruit.lower()
print(x)

#changing list
lotto = [2,14,26,41,63]

print(lotto)

lotto[2] = 28
print(lotto)

print(len(lotto))

print(range(len(lotto)))


#two loops same funcitons
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends: #goes through the list and pull out data.
    print('Happy new year', friend)

for i in range(len(friends)): #goes through list of [0,1,2] and the data inside it.
    friend = friends[i]
    print(' Happy new year', friend)
