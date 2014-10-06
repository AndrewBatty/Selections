# Andrew Batty
# Selection exercise:
# Development Exercise 2:
# 06/102014

temperature = int(input("Please enter the temperature of water in a container in degrees centigrade: "))

if temperature <= 0:
    print("The water is frozen.")
elif temperature >=100:
    print("The water is boiling.")
else:
    print("The water is neither boiling or frozen.")
    
