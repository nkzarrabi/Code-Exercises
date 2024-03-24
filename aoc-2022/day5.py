'''
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:
'''
text = {5: open('input5.txt').read(), 55: open('example5.txt').read()}

print(text[5])

input = text[5].strip()


# Parsing the stack configuration
def parse_stack_text(stacktext):
    stacks = [""]*10
    for line in stacktext[:-1]:
        for i, box in enumerate(line[1::4]):
            if box != " ": stacks[i+1] += box
    return stacks
    
input_data = input
stackt, instructions = [part.split("\n") for part in input_data.split("\n\n")]
stacks = parse_stack_text(stackt)

p1, p2 = stacks[:], stacks[:]
for line in instructions:
    _, n, _, src, _, dest = line.split()
    n = int(n); src = int(src); dest = int(dest)

    p1[src], p1[dest] = p1[src][n:],  p1[src][:n][::-1] + p1[dest]
    p2[src], p2[dest] = p2[src][n:],  p2[src][:n]       + p2[dest]

print("Part 1:", "".join(s[0] for s in p1 if s))
print("Part 2:", "".join(s[0] for s in p2 if s))