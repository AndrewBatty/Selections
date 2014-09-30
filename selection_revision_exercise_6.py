# Andrew Batty
# Selection Revision exercise: 6
# 30/09/2014

firstNumber = int(input("Please enter a number: "))
secoundNumber = int(input("Please enter anouther number: "))
thirdNumber = int(input("Please enter a third number: "))

if thirdNumber < firstNumber > secoundNumber:
    print("The largest of the three integers is: {0}".format(firstNumber))
elif firstNumber < secoundNumber > thirdNumber:
    print("The largest of the three integers is: {0}".format(secoundNumber))
elif firstNumber < thirdNumber > secoundNumber:
    print("The largest of the three integers is: {0}".format(thirdNumber))
    
