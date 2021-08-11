
# The task you have to perform is “Your Age In 2090”. This task consists of a total of 10 points to evaluate your performance.

# Problem Statement:-
# Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).

# Here are a few instructions that you must have to follow:


 
# Do not use any type of modules like DateTime or date utils. (-5 points)
# Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
# Your code should handle all sort of errors like:                       (2 points)
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other errors, if possible!

CurrentYear = 2020
while True:
    Age = int(input("\n\nPlease enter your birth of year or your age : "))

    if len(str(Age)) == 4 and Age > 1885 :
        if Age > CurrentYear:
            print("You are not yet born !\n\n")
            print("Please try again! \n\n")
            continue

        elif Age < 1920:
            print("OMG ! YOU ARE TOOOOOO OLD AND OLDEST PERSON LIVING !")

        elif Age < CurrentYear+1:
            temp = Age + 100
            print(f"You will turn 100 in {temp}\n\n")

        Tellage = int(input("Please enter a year so that we tell your age in that year : "))
    
        if Tellage < Age:
            print("Sorry, your are not yet born !")
        elif Tellage >= Age:
            temp = Tellage - Age
            print(f"You will be {temp} years old in {Tellage}")
        else:
            print("Wrong Input !")

    elif Age > 0 and len(str(Age)) < 4:
        if Age == 100:
            print("You are already 100 ! Congratulations\n\n")
        elif Age > 120:
            print("You are the oldest man living on Earth !!!\n\n")
        elif Age > 100:
            print("You are quite old and already crossed 100 !\n\n")
        elif Age < 100:
            temp = 100 - Age
            temp = CurrentYear + temp
            print(f"You will turn 100 in {temp}\n\n")

        Tellage = int(input("Please enter a year so that we tell your age in that year : "))
    
        temp = CurrentYear - Age
        if Tellage < temp:
            print("Sorry, your are not yet born !")
        elif Tellage >= temp:
            temp = Tellage - temp
            print(f"You will be {temp} years old in {Tellage}")
        else:
            print("Wrong Input !")
    
    else :
        print("The input provided by you is not valid !")
        continue

    Input1 = input("\nIf you want to quit program, enter \"quit\" in the field : ")
    if Input1 == "quit":
        exit()
