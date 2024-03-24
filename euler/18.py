#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

#3
#7 4
#2 4 6
#8 5 9 3

# i.e, 3 + 7 + 4 + 9 = 23.

import time

# Find the maximum total from top to bottom of the triangle below:
triangle = '''
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''


def e18():
    start = time.time()
    f= triangle.strip('\n').split('\n')
    summ=[75]
    for s in f:
        slst=s.split()
        lst=[int(item) for item in slst]
        for i in range(len(lst)):
            if i==0:
                lst[i]+=summ[i]
            elif i==len(lst)-1:
                lst[i]+=summ[i-1]
            elif (lst[i]+summ[i-1])>(lst[i]+summ[i]):
                lst[i]+=summ[i-1]
            else:
                lst[i]+=summ[i]
        summ=lst
    end = time.time() - start
    print("Runtime =", end)
    return max(summ)
print(e18()) #1074