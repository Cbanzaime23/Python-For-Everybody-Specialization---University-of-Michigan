hours = input("Enter Hours:")
rate = input("Enter Rate")

try:
    hours = float(hours)
    rate = float(rate)
except:
    hours = -1
    rate = -1
    print("Error, please enter numeric input")
    quit()

#print(hours,rate)

if hours <= 40:
	amount = hours * rate
else:
    diff = hours - 40
    amount = (hours * rate) + (diff * (rate * 0.5))

print(amount)


# score = input("Enter Score: ")
#
# score = float(score)
#
# if score < 0 and score > 1:
#     print("the score is out of range")
#     quit()
# elif score < 0.6:
#     print("F")
# elif score >= 0.6 and score < 0.70:
#     print("D")
# elif score >= 0.7 and score < 0.80:
#     print("C")
# elif score >= 0.8 and score < 0.90:
#     print("B")
# elif score >= 0.9 and score <= 1:
#     print("A")
