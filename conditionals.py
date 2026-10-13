# Conditional if/else logic- these are keywords that insturct your
# program to do specific instuctions based of specific data
# or conditions.


# conditional syntax( how it is written) 
bill_amount = int(input("please type a bill tender (1, 5, 10, 20): "))
# if usually indicates that someting is a possible option
if bill_amount == 1:
    print("here are 4 quarters")

# elif allows us to indicate that there are more possible options
# you can have as many elif as you want
elif bill_amount == 5:
    print("here are 20 quarters")

elif bill_amount == 10:
    print("here are 50 quarters")

elif bill_amount == 20:
    print("sorry cant accept your money, here's your money back")

# else is ALWAYS your last option.
else:
    print("sorry amount entered is not correct")

def college(): 
    grade= int(input(" please type in your grade: ")) 
    if grade > 90: 
        templeUApp() 


