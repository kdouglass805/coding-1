 # Function- simply put; a code block of
#instuctuons for computers to follow


# Built in functions - a code block of 
#instructions for a computer to follow 
#that was already written for us
#PRE -WRITTENcode instructions

from os import name


print('hello')
year = input("what year is it?")
print(year)

# input() a built in fucntion that allows a user tp
# type in data into the terminal. the data that is passed
# in will always be treated as a string data type.

# print() a built in fuction that allows a user to
# print data out in a terminal.

# name = "Good Morning" 
print (len (name ))

# Data casting functions
# these are built in (pre_written) functions
# that change data types from one form into another

year = 1906

# str() - this datacasting function allows yoU to change
# any data type into a string
year = 1906
print("This event took place in "+ str(year))

month = input("what numerical month were you born? ")


# float() - A function that will change any datatype
# passed into it, into float/ decimal number

num2 = input("type in a number: ")
# input always returns a string
print(9 + float(num2))