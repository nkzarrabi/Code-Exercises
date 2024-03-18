# The sum of the primes below 10 is 2+3+5+7=17.

# Find the sum of all the primes below two million.

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def sum_of_primes(n):
    sum = 0
    for i in range(2, n):
        if is_prime(i):
            sum += i
    return sum

print(sum_of_primes(10)) # 17
print(sum_of_primes(2000000)) # 142913828922
