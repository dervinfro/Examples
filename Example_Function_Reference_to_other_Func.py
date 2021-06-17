import numpy as np

'''
In the First_Function, I'm showing that I can name the var "Function.Var" and call that 
same "Function.Var" in the Second_Function.
This is all done WITHOUT a "return" in the First_Function.
'''

#%% First Section
# Define the first function.
def First_Function(mystr):
    X = mystr
    First_Function.x_var = np.log(X)
    print('First Fuction x var: ', First_Function.x_var, sep='\n')
    print('')

# Run First Function with var of 10
First_Function(10)


#%% Second Section
# Second Function that pulls in the First Function x var
def Second_Function():
    X2 = First_Function.x_var
    print('Second Function pulling in First Function: ', X2, sep='\n')
    print('')
    
# Run Second Function  
Second_Function()


#%% Third Section
def Third_Function(some_number):
    X3 = some_number **3
    X3_1 = np.log(some_number)
    X3_2 = 75**2
    
    # Make the return object a list
    return [X3, X3_1, X3_2] #if this "return" line is commented out, it returns: Fourth Func:  None

# Make the Function a list object
third_list = Third_Function(100)


#%% Fourth Section
def Fourth_Function():
    x4_var = Third_Function(100)
    # print('Fourth Func pulling in Third Function list: ', x4_var[0:2], sep='\n')
    # print('')
    
    return x4_var[0]

# The printing of this Fourth_Function will output the return value: 1000000
print('Fourth Function List - item 0: ', Fourth_Function(), sep='\n')

# This returns an integer of the return value: 1000000
fourthfunc_var = Fourth_Function()


#%% Fifth Section
def Fifth_Function(number):
    x5_var = np.square(number)
    
    # With the return enabled, the variable is 49 
    # With the return disabled, the variable is NoneType
    return x5_var

fifthfunc_var = Fifth_Function(7)
        