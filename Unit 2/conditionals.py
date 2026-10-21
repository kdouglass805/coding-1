# Conditional if/else logic- these are keywords that instruct your 
# program to do specific instructions based on specific data 
# or conditions

def billMachine():
# condititional syntax (how it is written)
    bill_amount = int(input("Please type in a bill tender (1,5,10): "))
# if usually indicates that something is a possible option
    if bill_amount == 1:
        print("here are 4 quarters")
# elif allows us to indicate that there are more possible options
# you can have as many elif as you want
    elif bill_amount == 5:
        print("here are 20 quarters")
    elif bill_amount == 10:
        print("here are 50 quarters")
    elif bill_amount == 20:
        print("sorry cant accepts 20s. here's your money back")
    elif bill_amount == 50:
        print("sorry cant accepts 50s. here's your money back")
# else is ALWAYS your last option. 
    else: 
        print("sorry amount entered is not correct. your burnt")


def college():
    grade=  int(input("please type in your grade: "))
    if grade > 90:
        templeUApp()
    else:
        ccpApp()

def ccpApp():
    print("congrats please complete the community college app with the following code")
    print("238293")

def templeUApp():
    print("congrats please complete the templa u app with the following code")
    print("a7ds78sd") 

college()



def calculate_add():
    print("program has strated: please type 2 numbers to add")
    num1 = int(input())
    num2 = int(input())
    print(num1 + num2)





def calculate_multiply():
    print("program has strated: please type 2 numbers to multiply")
    num1 = int(input())
    num2 = int(input())
    print(num1 * num2)



    def calculate_subtract():
     print("program has strated: please type 2 numbers to subtract")
    num1 = int(input())
    num2 = int(input())
    print(num1 - num2)


    def calculate_divide():
     print("program has strated: please type 2 numbers to divide")
    num1 = int(input())
    num2 = int(input())
    print(num1 / num2)



def movieTicket():
    print("Welcome to the movie theater. Please type in your age ")
    age = int(input())
    if age <= 7:
        print("your ticket is 8.00. ")
    elif age >= 8 and age <= 20:
        print('your ticket is 12.00') 
    elif age >= 21 and age <= 60:
        print('your ticket is 20.00')
    elif age >=61:
        print("your ticket is free. ")
    else:
        print("sorry there was an error in the program...")

movieTicket()






