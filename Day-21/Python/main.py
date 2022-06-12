import sys
from copy import deepcopy

m = [
    ['.', '#', '.'],
    ['.', '.', '#'],
    ['#', '#', '#']
]

def flip_horizontal(m):
    return list(map(lambda x: x[::-1], m.copy()))

def flip_vertical(m):
    return deepcopy(m[::-1])

def rotate(m):
    return [[m[j][-i-1] for j in range(len(m))] for i in range(len(m))]

def lts(m):
    return '/'.join(map(''.join, m))

def stl(s):
    return list(map(list, s.split('/')))

identity = lambda x: x
funs = [rotate, flip_horizontal, flip_vertical, identity]

rule = {}
for line in sys.stdin:
    a, b = line.strip().split(' => ')
    for f1 in funs.copy():
        for f2 in funs.copy():
            for f3 in funs.copy():
                rule[lts(f1(f2(f3(stl(a)))))] = b

size = len(m)
ons = [5]
for it in range(18):
    if size % 2 == 0:
        gran = 2
    elif size % 3 == 0:
        gran = 3
    new_m = [(['-'] * (size * (gran + 1) // gran)).copy() for _ in range(size * (gran + 1) // gran)]
    for i in range(size // gran):
        for j in range(size // gran):
            def do():
                for f1 in funs.copy():
                    for f2 in funs.copy():
                        for f3 in funs.copy():
                            t = lts(f1(f2(f3([[m[gran*i + k][gran*j + l] for l in range(gran)] for k in range(gran)]))))
                            if t in rule:
                                return rule[t]
            trans = stl(do())
            for k in range(gran + 1):
                for l in range(gran + 1):
                    new_m[(gran + 1)*i + k][(gran + 1)*j + l] = trans[k][l]
    m.clear()
    m.extend(new_m)
    size = size * (gran + 1) // gran
    ons.append(sum(map(lambda x: x.count('#'), m)))

print('Part 1:', ons[5])
print('Part 2:', ons[18])