# Largest Palindrome Product 
'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 * 99.
'''

#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]

largest_palindrome = 0 

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        p = i * j
        if isPalindrome(p):
            if p > largest_palindrome:
                largest_palindrome = p

print(largest_palindrome)
        