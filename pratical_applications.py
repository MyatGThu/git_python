import re

lin = 'From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'

y = re.findall('^From .*@([^ ]*)', lin)

print(y)
#spam confidence

hand = open('mbox-short.txt')

numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum: ', max(numlist))


#escape character = looking for a specific work / letter / sign

x = 'We just received $10.00 for cookies.'

y = re.findall('\$[0-9,]+', x)
print(y)
