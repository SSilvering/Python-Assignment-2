#===============================================================================#
#---------------------------Python Assignment 2---------------------------------# 
#                                                                               #
# Student 1:             Shai Hod     - 304800402                               #
# Student 2:             Dudu Abutbul - 200913671                               #
#===============================================================================#

#Question -4-

def Trapez_rule(f, a, b, n):
    """
    This method performs an integration based on 
    the trapezoidal rule, for a specific function.
    @param f: General function.
    @type f: function.
    @param a: Lower limit of the integral.
    @type a: Integer.
    @param b: Higher limit of the integral.
    @type b: Integer.
    @param n: Number of iteration. (Accuracy)
    @type n: Integer.
    """
    h = float(b - a) / n                          # Evaluate multiplication factor.
    tot = sum(f(a + h * i) for i in range(1, n))  # Calculate all the elements in epsilon.
    tot += (f(a) + f(b)) / 2.0                    # Add to the sum the first and last elements.
    return print(tot * h)                         # Multiplying the sum by the width of each rectangle.

Trapez_rule(lambda x:x ** 9, 0.0, 10.0, 100000)               # Execute line.
Trapez_rule(lambda x:x ** 4 + x ** 2 + 1, 0.0, 10.0, 100000)  # Execute line.

#------------------------------------------------------------------------------ 
#Question -5-

def myFilter(L, func):
    """
    This method gets a list of numbers and a function, 
    and returns a revised list includes only numbers for which the function returns true.
    @param L: List of numbers.
    @type L: List.
    @param func: A function.
    @type func: Function.
    """
    if not isinstance(L, list):  # Check if object is list.
        my_list = list(L)
    else:
        my_list = L
    
    result = []
    for _ in my_list:           # Iterate on all element in list.
        if func(_) == True:
            result.append(_)
    return result

#------------------------------------------------------------------------------ 

def myFilterMulti(L, funcL):
    """
    This method gets a list of numbers and a list of functions, 
    and triggers filtering based on those functions on the numbers in the list. 
    The function returns a revised list. 
    Filtering will be based on meeting all the conditions together.
    @param L: List of numbers.
    @type L: List.
    @param funcL: List of functions.
    @type funcL: List.
    """
    if not isinstance(L, list): # Check if object is list.
        my_list = list(L)
    else:
        my_list = L

    result = []                 #Initialize empty list.
    for _ in my_list:
        flag = True
        for func in funcL:
            if func(_) == False:
                flag = False
                break
        if flag:                #If the number has met all conditions it will be added to the new list.
            result.append(_)
            
    return result
            
#------------------------------------------------------------------------------ 

def myPrime(x):
    """
    This method checks if the number is a prime number.
    Returns True if is a prime number, otherwise returns False.
    @param x: A number.
    @type x: Integer.
    """
    if x < 2:                 #Returns false, if the number smaller than 2.
        return False
    
    if x == 2:                #Returns true for 2, the first prime prime number. 
        return True
    
    if x % 2 == 0:            #Returns false for other even number that different from 2.
        return False
    
    if x > 2:                 #Checks if the number has divider that provides an integer. 
        for _ in range(3, x):
            if x % _ == 0:
                return False

        return True

    return False              #Returns false for all other cases.

#------------------------------------------------------------------------------ 

def isFib(x):
    """
    This method gets a number and checks whether the number is in the Fibonacci sequence. 
    Returns true if yes, otherwise returns false.
    @param x: A number.
    @type x: Integer.
    """
    if x < 0:                                # Return false for negative numbers.
        return False
    if x == 0 or x == 1 or x == 2or x == 3:  # Returns true for the first four numbers series. 
        return True
    
    prev, cur = 1, 0                         # Initialize variables for calculate the elements in the series.
    
    for _ in range(1, x + 1):
        prev, cur = cur, prev + cur
        if cur == x:
            return True    
    
    return False                            #Returns false for all other cases.
    
#------------------------------------------------------------------------------ 
print(myFilter([2, 4, 5, 6], myPrime))
print(myFilterMulti([2, 4, 5, 6, 7, 13], [myPrime, isFib]))
print(myFilterMulti ([2, 4, 5, 13, 41, 55, 89, 107, 144], [myPrime, isFib, lambda x:len(str(abs(x))) == 2 ]))
#------------------------------------------------------------------------------ 
#Question -6-


