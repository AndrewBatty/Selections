# Andrew Batty
# selection Development Exercise 4
# 06/10/2014

marks = int(input("Please enter the mark you got for the maths exam: "))

if 0 <= marks < 40:
    print("You got a grade U.")
elif 41 <= marks < 50:
    print("You got a grade E.")
elif 51 <= marks < 60:
    print("You got a grade D.")
elif 61 <= marks < 70:
    print("You got a grade C.")
elif 71 <= marks < 80:
    print("You got a grade B.")
elif 81 <= marks < 100:
    print("You got a grade A.")
