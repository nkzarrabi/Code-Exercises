'''
<p>A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of $28$ would be $1 + 2 + 4 + 7 + 14 = 28$, which means that $28$ is a perfect number.</p>
<p>A number $n$ is called deficient if the sum of its proper divisors is less than $n$ and it is called abundant if this sum exceeds $n$.</p>

<p>As $12$ is the smallest abundant number, $1 + 2 + 3 + 4 + 6 = 16$, the smallest number that can be written as the sum of two abundant numbers is $24$. By mathematical analysis, it can be shown that all integers greater than $28123$ can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.</p>
<p>Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.</p>


'''

from itertools import combinations_with_replacement

# Function to find the sum of proper divisors of a number
def sum_of_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

# Function to check if a number is abundant
def is_abundant(n):
    return sum_of_divisors(n) > n

# Generating a list of abundant numbers up to 28123
abundant_numbers = [i for i in range(1, 28124) if is_abundant(i)]

# Generating all possible sums of two abundant numbers
abundant_sums = {sum(comb) for comb in combinations_with_replacement(abundant_numbers, 2) if sum(comb) <= 28123}

# Finding all numbers which cannot be expressed as the sum of two abundant numbers
non_abundant_sums = [i for i in range(1, 28124) if i not in abundant_sums]

# Calculating the sum of these numbers
total_sum = sum(non_abundant_sums)
print(total_sum)