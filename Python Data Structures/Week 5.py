#Dictionaries
#Key Value Pair
# purse = dict()
# purse['money'] = 12
# purse['candy'] = 3
# purse['tissue'] = 75
# print(purse['candy'])
#
# purse['candy'] = purse['candy'] + 7
# print(purse)
#
#
# jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
# print(jjj['chuck'])


#Dictionaries Application


# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
# print(counts)
#
#
# #Much simpler code
# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)


# counts = dict()
# print("Enter a line of text:")
# line = input('')
#
# words = line.split()
#
# print('Words:', words)
#
# print('Counting...')
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print('Counts', counts)


# counts = {'chuck': 1, 'fred': 42, 'jan': 100}
# for key in counts:
#     print(key, counts[key])

#
# jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
# # print(list(jjj))
# #
# # print(jjj.keys())
# #
# # print(jjj.values())
# #
# # print(jjj.items())
# for aaa, bbb in jjj.items():
#     print(aaa,bbb)





# name = input('Enter file:')
# handle = open(name)
#
# count = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
#
# bigcount = None
# bigcount = None
# for word, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
#
# print(bigword, bigcount)

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
counts = {}
for line in fh:
    if line.startswith('From') and not line.startswith('From:') :
        words = line.split()
        email = words[1]
        #pieces = email.split('@')
        counts[email] = counts.get(email, 0) + 1
        #print(counts)
        #count += 1

bigword = None
bigcount = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

#print("There were", count, "lines in the file with From as the first word")
