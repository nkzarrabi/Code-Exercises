
text = {22: open('euler/names.txt').read()}

#print(text[22])
input = text[22]
sorted_names = sorted(input.replace('"', '').split(','))
print(sorted_names)

# The ord() function returns an integer representing the Unicode character.
#print(ord('C'))

d= {chr(i): i - 64 for i in range(65, 91)}
print(d)
filtered_names = ([*name] for name in sorted_names if name != '')
print(filtered_names)

def e22(names):
    sum = 0
    for i, name in enumerate(names, 1):
        for x in name:
            sum += i*d[x]

    return sum




print(e22(filtered_names))