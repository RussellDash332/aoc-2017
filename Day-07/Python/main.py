import sys
from collections import deque

val = {}
indeg = {}
g = {}

for line in sys.stdin:
    if line.find('->') != -1:
        d, n = line.strip().split(' -> ')
        n = n.split(', ')
        d, v = d.split()
        v = int(v[1:-1])
        val[d] = v
        g[d] = n
        for nn in n:
            indeg[nn] = indeg.get(nn, 0) + 1
        indeg[d] = indeg.get(d, 0)
    else:
        d, v = line.strip().split()
        v = int(v[1:-1])
        val[d] = v
s = list(filter(lambda x: indeg[x] == 0, indeg))[0]
print('Part 1:', s)

def weight(pos):
    if pos not in g:
        return val[pos]
    return val[pos] + sum(map(weight, g[pos]))

def check(p):
    sus = []
    def helper(pos, num):
        if pos in g:
            w = list(map(weight, g[pos]))
            sus.append((pos, num))
            if len(set(w)) != 1:
                freq = {}
                for i in w:
                    freq[i] = freq.get(i, 0) + 1
                for i in freq:
                    if freq[i] == 1:
                        impostor = i
                    else:
                        actual = i
                for i in range(len(w)):
                    if w[i] == impostor:
                        helper(g[pos][i], actual - impostor)
    helper(p, 0)
    return val[sus[-1][0]] + sus[-1][1]
print('Part 2:', check(s))