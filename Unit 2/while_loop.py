# Loop - a loop is a construct (special function) that repeats itself,
#- in a program, a loop allows to repeat code instructions.

# There are two types of loops: For loop and while loop and while loop

# WHile loop - a type of loop where so long as a  condition is equal
# tp true it will keep running forever.

# the keyword is while --> do while

# # syntax
# num = 4
# while 2+2 == num: # condition --> operantions 
#  print(" the program is running...")
#  num = int(input("please type in a new number: "))

    # while loops will ALWAYS run unless you change the condition!
    # we can do this by writing instructions to maually change it.



# while userGuess != correctAnswer:
#     print("sorry thats incorrect")
#     print("try again...")
#     attempts +=1
#     print("number of attempts: " + str(attempts))
#     userGuess= int(input("please type in a number to guess:"))

# print("congraulations you guessed correctly!")
# print(" do you want to try again")

#guessingGame()



def passwordreset():
    correctPassword = "KadenD"
    atempts = 4

    print("please log in with your password:")
    userPawAttempt = input()

    while userPwattempt != correctPw:
        print("sorry incorrect password")
        print("please try again")
        