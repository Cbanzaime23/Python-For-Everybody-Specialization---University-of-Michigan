import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    for words in string:
        num = re.findall('\$[0-9.]+', words)
        #if len(stuff) != 1 :  continue
        num = float(stuff[0])
        numlist.append(num)
print('Sum:', sum(numlist))
