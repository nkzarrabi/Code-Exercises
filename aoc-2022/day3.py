
text ={3: open('input3.txt').read()}

#print(text[3])

practice_text = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''

#print(practice_text)
#priorities is range(1,27) for lowercase item types a to z
#priorities is range(27,53) for uppercase item types A to Z


puzzle = text[3]
priorities = {chr(i): i-96 for i in range(97, 123)}
priorities.update({chr(i): i-38 for i in range(65, 91)})

#print(priorities)
sum = 0
for rucksack in puzzle.splitlines():
    #print(rucksack)
    #print(rucksack.split())
    for sack in rucksack.split():
        N = len(sack) // 2
        #print(N)
        compartment1, compartment2 = sack[:N], sack[N:]
        #print(compartment1, compartment2)
        setz = set(compartment1).intersection(compartment2)
        #print(setz)
        for i in setz:
            sum += priorities[i]

print(sum)

### Part 2

sum2 = 0    
group = []
l = []
puzzle = text[3]
for rucksack in puzzle.splitlines():
    for sack in rucksack.split():
        l.append(sack)
        if len(l) % 3 == 0:
            #print(len(l))
            group.append(l)
            l = []
        
        

#print(group)
for i in group:
    setz = set(i[0]).intersection(i[1]).intersection(i[2])
    for i in setz:
        sum2 += priorities[i]

print(sum2)