# friends = ['Joseph', 'Glen', 'Sally']
#
# for friend in friends:
#     print('Happy New Year:', friend)
#
# for i in range(len(friends)):
#     friend = friends[i]
#     print('Happy New Year:', friend)


#Manual average
# total = 0
# count = 0
#
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     total = total + value
#     count = count +1
#
# average = total / count
# print('Average:', average)

# numlist = list()
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     numlist.append(value)
#
# average = sum(numlist) / len(numlist)
# print('Average:', average)

line = 'A lot                   of spaces'
etc = line.split()
print(etc)

line = 'first;second;third'
thing = line.split()
print(thing)

print(len(thing))

thing = line.split(';')
print(thing)
print(len(thing))


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2], words[3], words[6])



The Double split Pattern

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split ()
email = words[1]
pieces = email.split('@')
print(pieces[1])



#Assignment 1

# fname = input("Enter file name: ")
# #fname = "romeo.txt"
# fh = open(fname)
# lst = list()
# for line in fh:
#     Words = line.split()
#     for word in Words:
#         if word not in lst:
#             lst.append(word)
# lst = sorted(lst)
# print(lst)


#Assignment 2

# fname = input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"
# count = 0
# fh = open(fname)
# for line in fh:
#     if line.startswith('From') and not line.startswith('From:') :
#         words = line.split()
#         email = words[1]
#         #pieces = email.split('@')
#         print(email)
#         count += 1
#
# print("There were", count, "lines in the file with From as the first word")
#

# line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# words = line.split ()
# email = words[1]
# pieces = email.split('@')
# print(pieces[1])


stuff = dict()
print(stuff['candy'])
