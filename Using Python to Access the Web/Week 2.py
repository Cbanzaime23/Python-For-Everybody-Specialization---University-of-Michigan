#Using re.search() Like find()
#
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     #Check is a line contains the word "From:"
#     if line.find('From:') >= 0:
#         print(line)



# import re
#
# hand =open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('From:', line):
#         print(line)

#Using re.search() Like startswith()
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     #Check is a line contains the word "From:"
#     if line.startswith('From:'):
#         print(line)


# import re
#
# hand =open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^From:', line):
#         print(line)


# import re
# x = 'My 2 favorite numbers are 19 and 42'
# y = re.findall('[0-9]+', x)
# print(y)
#
# y = re.findall('[AEIOUM]+', x)
# print(y)

#Greedy Matching
# import re
# x = 'From: Using the : character:'
# y = re.findall('^F.+:', x)
# print(y)
#
#
# #Not Greedy Matching
# import re
# x = 'From: Using the :character'
# y = re.findall('F.+?:', x)
# print(y)
#
#
# x = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
# y = re.findall('\S+@\S+', x)
# print(y)
# y = re.findall('^From (\S+@\S+)', x)
# print(y)
#

#Using find
# data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
# atpos = data.find('@')
# print(atpos)
#
# sppos = data.find(' ', atpos)
# print(sppos)
#
# host = data[atpos+1 :  sppos]
# print(host)
#
#
# #The Double Split Pattern
# words = data.split(' ')
# email = words[1]
# pieces = email.split('@')
# print(pieces[1])
#
#
# import re
# data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
# y = re.findall('@([^ ]*)', data)
# print(y)
#
# y = re.findall('^From .*@([^ ]*)', data)
# print(y)



# import re
# hand = open('mbox-short.txt')
# numlist = list()
# for line in hand:
#     line = line.rstrip()
#     stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
#     if len(stuff) != 1 :  continue
#     num = float(stuff[0])
#     numlist.append(num)
# print('Maximum:', max(numlist))
#
# import re
# x  = 'We just received 10000 for cookies  100000'
# y = re.findall('[0-9]+', x)
# print(y)


import re
hand = open('regex_sum_1071439.txt')
numlist = list()
count = 0
for line in hand:
    line = line.rstrip()
    nums= re.findall('[0-9]+', line)
    for num in nums:
        num = float(num)
        print(num)
        numlist.append(num)
        count = count+ 1
print('Sum:', sum(numlist))
print(count)


#import re
#print( sum( [num for (for line in ('[0-9]+',('regex_sum_1071439.txt').read())) ] ) )
#print(  [num for (line for line in ('[0-9]+',('regex_sum_1071439.txt').read())) ] )
