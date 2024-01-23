maximum = None
minimum = None

while True:
    val = input("Enter a number:")
    if val == 'done':
        break
    try:
        fval = float(val)
        
        #smallest
        if minimum is None:
            minimum = fval
        elif fval < minimum:
            minimum = fval

        #largest
        if maximum is None:
            maximum = fval
        elif fval > maximum:
            maximum = fval
    except:
        print("Invalid Input")
        continue





print("Maximum is", maximum)
print("Minimum is", minimum)