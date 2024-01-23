xfile = open('Sample Text File.txt')
# for cheese in xfile:
#     print(cheese)
#inp = xfile.read()
#print(len(inp))
# for line in xfile:
#     line = line.strip()
#     if line.startswith('Hello'):
#         print(line)


# for line in xfile:
#     line = line.rstrip()
#     if not line.startswith('Hi'):
#         continue
#     print(line)
#
# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     quit()
#
# count = 0
# for line in fhand:
#     if line.startswith('Hello'):
#         count = count + 1
# print('There were', count, 'subject lines in', fname)

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
counter = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        dot = line.find('.')
        extract = line[dot - 1:  dot + 5]
        extract = float(extract)

        total = total + extract
        counter = counter + 1

average = total / counter
print("Average spam confidence: " + str(average))
