import sys
from heapq import *

ports = []
g = {}
for line in sys.stdin:
    a, b = map(int, line.split('/'))
    g[a] = g.get(a, []) + [b]
    g[b] = g.get(b, []) + [a]
    ports.append((a, b) if a <= b else (b, a))

def gen_all(state):
    bridges = [state]
    s, a, used = state
    for b in g[a]:
        check = (a, b) if a <= b else (b, a)
        if check not in used: # assuming all components are different, which is the case
            bridges.extend(gen_all((s + a + b, b, used | {check})))
    return bridges

bridges = gen_all((0, 0, set()))
print('Part 1:', sorted(bridges, key=lambda x: -x[0])[0][0])
print('Part 2:', sorted(bridges, key=lambda x: (-len(x[2]), -x[0]))[0][0])