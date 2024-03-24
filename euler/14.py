'''The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13
, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 
It can be seen that this sequence (starting at 13
 and finishing at 1
) contains 10 
 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''

def collatz(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

def collatz_chain(n):
    count = 1
    while n != 1:
        n = collatz(n)
        count += 1
    return count

def longest_collatz_chain(limit):
    longest_chain = 0
    starting_number = 0
    for i in range(1, limit):
        chain = collatz_chain(i)
        if chain > longest_chain:
            longest_chain = chain
            starting_number = i
    return starting_number

print(longest_collatz_chain(1000000))