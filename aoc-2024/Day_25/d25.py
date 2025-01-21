
flag = False
file = 'example2.txt' if flag else 'input.txt'
file = open(file, 'r')

def parse(f):
    locks = []
    keys = []
    for group in f.read().split('\n\n'):
        lines = group.split()
        ident = tuple(col.count('#') - 1 for col in zip(*lines))
        (keys, locks)[lines[0] == '#####'].append(ident)
    return locks, keys

def fits(lock, key):
    return all(l + k <= 5 for l, k in zip(lock, key))

locks, keys = parse(file)
print(sum(fits(lock, key) for lock in locks for key in keys))