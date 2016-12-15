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
