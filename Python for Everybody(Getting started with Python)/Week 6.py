def computepay(hours,rate):

    #print(hours,rate)
        if hours <= 40:
            amount = hours * rate
        else:
            diff = hours - 40
            amount = (hours * rate) + (diff * (rate * 0.5))

        return amount


hours = input("Enter Hours:")
rate = input("Enter rate:")

try:
    hours = float(hours)
    rate = float(rate)
except:
    hours = -1
    rate = -1
    print("Error, please enter numeric input")
    quit()

p = computepay(hours,rate)
print("Pay",p)
