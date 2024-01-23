#Tuples are like list

# x = ('Glenn', 'Sally', 'Joseph')
# print(x[2])
# y = (1,9,2)
# print(max(y))
#
# #List are mutable, Tuples and String are not
#
# #Tuples and Assignment
# (x, y) = (4, 'fred')
# print(y)


# d = dict()
# d['csev'] = 2
# d['cwen'] = 4
#
# for (k,v) in d.items():
#     print(k,v)
#
# tups = d.items()
# print(tups)

#Sort by Key
# d = { 'b':1, 'c':22,'a':10}
# t = sorted(d.items())
#
# for k,v in sorted(d.items()):
#     print(k,v)


#Sorted by values
# c = {'a':10, 'b':1, 'c':22}
# tmp = list()
# for k,v in c.items():
#     tmp.append((v,k))
#
# print(tmp)
#
# tmp = sorted(tmp, reverse = True)
# print(tmp)


# fhand = open('romeo.txt')
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
#print(counts)
#
# lst = list()
# for key, val in counts.items():
#     newtub = (val, key)
#     lst.append(newtub)
#
# #print(lst)
#
# lst = sorted(lst, reverse = True)
# print(lst)
#
# #Print Top 10
# for val, key in lst[:10]:
#     print(key, val)







# c = {'a':10, 'b':1, 'c':22}
#
# print(sorted([(v,k) for k,v in counts.items()], reverse = True))






# x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
# y = x.items()
# print(y)


fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
counts = {}
for line in fh:
    if line.startswith('From') and not line.startswith('From:') :
        words = line.split()
        time = words[5]
        time = time.split(':')
        hour = time[0]
        counts[hour] = counts.get(hour, 0) + 1
#print(counts)

lst = list()
for key, val in counts.items():
    newtub = (key, val )
    lst.append(newtub)

#print(lst)

lst = sorted(lst, reverse = False)
print(lst)

#Print in decending order of values
for key, val in lst:
    print(key, val)




# bigword = None
# bigcount = None
# for word, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
#
# print(bigword, bigcount)
