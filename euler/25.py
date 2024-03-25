'''
The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 
12 terms will be:
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
 
The 12
th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 
 digits

'''

# Variables to store the current index, and the first two Fibonacci numbers
index, a, b = 2, 1, 1

# Loop until we find a Fibonacci number with 1000 digits
while len(str(b)) < 1000:
    a, b = b, a + b
    index += 1

print(index)