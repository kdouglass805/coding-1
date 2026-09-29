
from ctypes.wintypes import BOOLEAN


print(200 == 100 ) #False

print( 15 < 18) #true


print("Coding 1" == "coding 1") #false


print("0" == 0 ) #true






Book = 10.99
Tablet = 399.99

print(Book + Tablet)



cart = 98.97 
amountToGetDiscount = 100.00

print( cart > amountToGetDiscount ) # false



shoes = 200.00
tax = 0.07

print(shoes * tax) # 14.00



GPA = 86
Reconmmendation = 85

print(GPA> BOOLEAN) # true



GPA = 86
Reconmendation = False
print(GPA > 85  and Reconmendation == True) 