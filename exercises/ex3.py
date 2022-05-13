ival  = input('Enter your age:')

try:
    w = int(ival)
except:
    w = -1

if w > 0 :
    print('Its a number')
else:
    print('Not a number')
