#Multiples of 3 or 5 

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000. 
'''


n1 = 999 // 3
n2 = 999 // 5
n3 = 999 // 15

sum1 = 3 * n1 * (n1 + 1) // 2
sum2 = 5 * n2 * (n2 + 1) // 2
sum3 = 15 * n3 * (n3 + 1) // 2

print(sum1 + sum2 - sum3)