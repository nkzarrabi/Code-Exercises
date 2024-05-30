import time
import math


def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2  # i and n/i
    if math.isclose(n**0.5, int(n**0.5), rel_tol=1e-09, abs_tol=0.0):  # Perfect square
        count -= 1  # Correct the double counting of the square root
    return count

def find_triangle_number(divisor_target):
    n = 1
    while True:
        # Calculate the nth triangle number
        triangle_number = n * (n + 1) // 2
        
        # Check if n is even to split the factors between n and n+1
        if n % 2 == 0:
            count_n = count_divisors(n // 2)
            count_n_plus_1 = count_divisors(n + 1)
        else:
            count_n = count_divisors(n)
            count_n_plus_1 = count_divisors((n + 1) // 2)
        
        # If the number of divisors exceeds the target, return the triangle number
        if count_n * count_n_plus_1 > divisor_target:
            return triangle_number
        
        n += 1

# Find the first triangle number with over 500 divisors




start = time.time()
index = find_triangle_number(500)
elapsed = (time.time() - start)

print("result %s returned in %s seconds." % (index, elapsed))
