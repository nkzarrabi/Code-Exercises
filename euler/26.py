'''
A unit fraction contains 1
 in the numerator. The decimal representation of the unit fractions with denominators 2
 to 10 are given:
1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10 =  0.1
'''

#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def e26():
    max_cycle = 0
    d = 0
    for i in range(2, 1000):
        remainders = []
        remainder = 1
        while remainder not in remainders:
            remainders.append(remainder)
            remainder = (remainder * 10) % i
        if len(remainders) - remainders.index(remainder) > max_cycle:
            max_cycle = len(remainders) - remainders.index(remainder)
            d = i
    return d

print(e26())