
def sum_of_digits(n):
    return sum(int(x) for x in str(n))

print(sum_of_digits(2**15))  # 26
print(sum_of_digits(2**1000))  # 1366
