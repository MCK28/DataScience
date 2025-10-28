'''This module contains useful mathematical functions and variables'''

# Define a function that performs the factorial operation.
def factorial3(x):
    '''this function calculates factorial of a given number.'''
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial3(x - 1)
    

# Define a function that calculates n number of elements in a fibonacci series
def fib_serias(n):
    '''Returns the fibonacci series with n elements'''
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        next_element = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_element)
    return fibonacci

# Define a function that calculates the square root of a given integer
def sqroot2(x):
    return x**0.5

# Define a function that performs power operation
def power(x, y):
    '''This function performs power or exponent operation on two given numbers,
     it raises x to the power of y '''
    return x ** y

# Variable 
pi = 3.14
e = 2.7