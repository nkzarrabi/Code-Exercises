from collections import Counter 

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


#list1 = [2520 % (i+1) ==0 for i in range(10)]

#print(list1)

primes_below_20 = [2,3,5,7,11,13,17,19]

def prime_factors(n, primes_below_n = primes_below_20):
    if n == 1:
        return []
    for prime in primes_below_n:
        if n % prime == 0:
            return [prime] + prime_factors(n // prime)
        
primes_needed = Counter()

for n in range(2,21):
    primes = Counter(prime_factors(n))
    primes_needed |= primes 

total = 1 
for p, amount in primes_needed.items():
    total *= p ** amount

print(total)


l2 = [232792560 % (2*i) == 0 for i in range(1, 11)]

print(l2)