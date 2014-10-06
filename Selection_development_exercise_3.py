# Andrew Batty
# Selection Development Exercise 3:
# 06/10/2014

print("This program will take the number of hours you have worked this week and you standad hourly rate, and increase the pay for the hours above 40 by 1.5 times.")

hours = int(input("Please enter the number of hours you worked this week: "))
rate = float(input("Please enter your standard rate of hourly pay: "))

extra = hours - 40
extraRate = rate * extra * 1.5
normalRate = hours * rate
normalPay = 40 * rate
extraPay = extraRate + normalPay

if 0 < hours and hours > 60:
        print("The hours you have worked are not in range.")
elif hours > 40:
        print("Youe total pay for this week is is {0}".format(extraPay))
else:
    print("Your toatal pay for this week is {0}".format(normalRate))
