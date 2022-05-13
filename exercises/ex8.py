han = open('mbox-short.txt')

for line in han:

    line = line.rstrip()
    wds = line.split()
# Skip Blank condition
#    if line == ' ':
#        print('Skip Blank')
#        continue

    #Guardian Pattern Better than the skip if blank condition above.
#    if len(wds) < 1:
#         continue
    if len(wds)< 3 or wds[0] != 'From':
        continue
    print(wds[2])
