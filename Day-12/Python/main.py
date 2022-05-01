import sys

class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
        self.size = [1 for _ in range(N)]
        self.num_sets = N

    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]

    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)

    def union(self, i, j):
        if not self.is_same_set(i, j):
            self.num_sets -= 1
            x, y = self.find_set(i), self.find_set(j)
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
                self.size[x] += self.size[y]
            else:
                self.p[x] = y
                self.size[y] += self.size[x]
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

g = {}
seen = set()
for line in sys.stdin:
    u, v = line.split('<->')
    v = map(int, v.split(', '))
    u = int(u)
    for i in v:
        g[u] = g.get(u, set()) | {i}
        g[i] = g.get(i, set()) | {u}
        seen.add(i)
    seen.add(u)
ufds = UFDS(max(seen) + 1)
for i in g:
    for j in g[i]:
        ufds.union(i, j)
print('Part 1:', ufds.size[ufds.find_set(0)])
print('Part 2:', ufds.num_sets)