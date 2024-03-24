
# starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.
# How many routes are there through a 20x20 grid?

# The number of routes from the top left corner to the bottom right corner of a grid is the central binomial coefficient of the grid's dimensions. The central binomial coefficient is given by the formula (2n)! / (n!)^2. For a 20x20 grid, this is 40! / 20!^2.

import math

def central_binomial_coefficient(n):
    return math.factorial(2 * n) // (math.factorial(n) ** 2)

print(central_binomial_coefficient(2))
print(central_binomial_coefficient(20))