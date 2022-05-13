# in operator
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip() #removing whie space
    if not '@uct.ac.ra' in line:
        continue
    print(line) #shows new line after each end.

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count: ', count)

#whole file

fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))

# print(inp[:10])

#through a file

fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line) #shows new line after each end.


#through a file [fixed]
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip() #removing whie space
    if not line.startswith('From:'):
        continue
    print(line) #shows new line after each end.
