# n = 50
# while n > 0:
#     print(n)
#     n = n - 1
# print('Blast,off!')
# print(n)


#Largest Number
LargestNum = 0
# for i in [2,4,6,1,5,3,-1,9, 70]:
#     if i > LargestNum:
#         LargestNum = i
# print(LargestNum)

#Running Total
# zork = 0
# print("Before", zork)
# for thing in [9, 41, 12, 3, 74, 15]:
#     zork = zork + thing
#     print(zork, thing)
#
# print('After', zork)

# count = 0
# sum = 0
# print("Before", count, sum)
#
# for val in [9, 41, 12, 3, 74, 15]:
#     count = count + 1
#     sum = sum + val
#     print(count, sum, val)
# print('After', count, sum,sum / count)


#Finding the smallest
# smallest = None #Flag value
# print('Before')
# for value in [9, 41, 12, 3, 74, 15]:
#     if smallest is None:
#         smallest = value
#     elif value < smallest:
#         smallest = value
#     print(smallest, value)
# print('After', smallest)


# num = 0
# total = 0.0
#
# while True:
#     val = input("Enter a number:")
#     if val == 'done':
#         break
#     try:
#         fval = float(val)
#         print(fval)
#         num = num + 1
#         total = total + fval
#     except:
#         print("Invalid Input")
#         continue
#
#
# print(total, num, total/num)




maximum = None
minimum = None

while True:
    val = input("Enter a number:")
    if val == 'done':
        break
    try:
        fval = float(val)
    except:
        print("Invalid Input")
        continue


        #smallest
        if minimum is None:
            minimum = fval
        elif value < minimum:
            minimum = fval

        #largest
        if maximum is None:
            maximum = fval
        elif value > maximum:
            maximum = fval


print("Maximum is", maximum)
print("Minimum is", minimum)
