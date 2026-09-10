# Assignment Operators- Exclusively used to
# assign vaules to variables.
#key / vaule pairings

# We used a single equal sign to repersent the assignment
# oprator
name = 'kaden'
grade = 10
school = True

# Arithmetic Operators- Used on numerical
# data types to perform calculations.
# Intergers ( whole numbers) and floats ( decimal mumbers)

# print is a function that lets us show code
# in the terminal

print(3 + 3) # additon operator
print(4 - 4) # subtraction operator
print( 12/ 4) # division operator
print (4 * 4 ) # multiplication operator

# Comparison Operators - set of symbols used
# assess if data is the same or different and
# how they differ

print(10 > 1) # greater than operator
print(10 < 1) # less than operator

# 2 equal signs compare if something is the same
print("kaden" == "Kaden") # same as (false)
print("2" == 2) # same as (false) not the same datatypes
print(2.0 == 2) # same as (true)


# not equal is written with !=
# this is to check and filter for vaules that are not
# the same
print(200 != 100) # True- these are not the same
print(300 != 300) # these are the same\

# logical operators- compares 2 conditions to check if 
# they are true or false

# AND- checks if 2 conditions are true. if yes, the final
# result if true
print(3 < 1 and 100 > 50) # this would come out to be true

# OR- checks if omly 1 condition is true. if yes ,
# the final result will be true
print( 3 > 1 or 100 > 50)


# NOT - "the opposite day". it will reserve the 
# result of the logical operators
print(not(3 > 1 and 100 > 50))
#this would come out to be false