import math
sum=0
for i in range(1,1001):
    sum += 1/(math.sqrt(10*i) + math.sqrt(10*i-10))

print(sum)
