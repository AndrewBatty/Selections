# Andrew Batty
# selection Development Exercise 4
# 06/10/2014

marks = int(input("Please enter the mark you got for the maths exam: "))

if 0 > marks < 40:
    print("The grade you got is a U.")
elif 41 > marks < 50:
    print("The grade you got is an E.")
elif 51 > marks < 60:
    print("The grade you got is a D.")
elif 61 > marks < 70:
    print("The grade you got is a C.")
