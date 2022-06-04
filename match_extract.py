import re

x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+', x)

print(y)


y = re.findall('{AEIOU}+', x)

print(y)

x = 'From: Using the : character' #Greedy Matching prints out larger result
y = re.findall('^F.+:',x )
print(y)


x = 'From: Using the : character' #Non-Greedy Matching prints out larger result
y = re.findall('^F.+?:',x )
print(y)
