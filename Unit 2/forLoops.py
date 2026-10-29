# What is a loopa --> Code that repeats.

# While loops = a block code that represents itself until the triggering
# condtion is no longer TRUE. CAN BE INFINITE

# For loops = a type of loop (code block that repeats itself.) BUT
# it only repeats itself upto a certain number of times. IT IS INFINITE

# THINK OF FOR LOOPS AS THE COUNTING LOOP

# FOR LOOP SYNTAX
# i stand for iterator = programmers decided to make this the universal
# symbol for a placeholder for counting


for i in range(1,6000):
    print(i)


# LIST --> a data collection type that acts as a conatiner for 
# multiple data types 

foodItem_1 = "apple"

groceryList = ["apples" , "oranges", "water", "chips", "groundbeef"]

print(groceryList)

for i in groceryList:
    print("I need to buy" + i)

grades = [ 100, 98, 75, 89, 80]

for i in grades:
    # show me the grades lower than 85
    if grades< 85:
        print (grades)