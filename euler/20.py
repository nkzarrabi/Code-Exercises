
# Load the factorial function 
# n! = n * (n-1) * (n-2) * ... * 1
from math import factorial

'''
10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800
The sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
Find the sum of the digits in the number 100!

'''
def e20():
    return sum(int(i) for i in str(factorial(100)))

print(e20())