


example= '''
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''




text = {1: open('input1.txt').read().split('\n\n'), 11: open('example1.txt').read().split('\n\n')}

#print(text[1])
l = [list(map(int, line.strip().split("\n"))) for line in text[1]]
#print(l)

l2 = [sum(list(map(int, line.strip().split("\n")))) for line in text[11]]
print(l2)

print(max(l2))

s = [sum(x) for x in l]
print(s)

print(max(s))

print(sum(sorted(s)[-3:]))