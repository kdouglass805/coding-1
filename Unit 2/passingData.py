# when we are building complex programs, we need a
# way to pass in dtat that is NOT always
# from the user.

## Function arguments and parameters are ways to
# pass in data that is NOT always
# from the user.

# Function arguments and parameters are ways to
# pass in data to a function from possibly
# another function.

# Function parametrs- this is PLACEHOLDER DATA for 
# a function. Variables inside the curly brackets
 

# memory trick - PARAMETER AND PLACEHOLDER BOTH
# START WITH THE LETTER P
def check_water_depth(depth):
    print(depth)
    print(depth > 10) # true if depth is greater than 10 feet
    # return depth


    # Function agruments- this is the REAL DATA that we pass into
    # the function call.
    # memory trick- if you make a REAL world agrument with a person
    # you need to come with REAL facts (data)
    check_water_depth(3)

# retun- this keyword allows us to pass data from INSIDE 1 function
# into another function

def username(name):
    return name

def confirmLogin(username):
    name = username(username)
    print(name)