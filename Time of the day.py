number = int(input("Tell me the hour and I will tell you the time of the day: "))

if number >= 5 and number < 11:
    print("It is morning!")    
elif number > 12 and number < 16:
    print("it is in the afternoon!")
elif number > 17 and number < 20:
    print("It is in the evening!")
elif number > 21 or number < 5:
    print("Night time! good night!")
elif number > 24:
    print("please enter a number from 1 - 24!")
else:
    print("You must enter only numbers")
