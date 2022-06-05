SIZE = 256

def kh(ss):
    bytes = list(map(ord, ss)) + [17, 31, 73, 47, 23]
    curr = skip = 0
    cl = list(range(SIZE))
    for _ in range(64):
        for length in bytes:
            s, e = curr, curr + length
            if e <= SIZE:
                cl[s:e] = cl[s:e][::-1]
            else:
                cl *= 2
                cl[s:e] = cl[s:e][::-1]
                cl[:e-SIZE] = cl[SIZE:e]
                cl = cl[:SIZE]
            curr = (curr + length + skip) % SIZE
            skip += 1
    xors = []
    for i in range(16):
        m = cl[16*i + 15]
        for j in range(15):
            m ^= cl[16*i + j]
        xors.append(hex(m)[2:].zfill(2))
    return list(''.join(map(lambda x: bin(int(x, 16))[2:].zfill(4), ''.join(xors))))

ss = input()
m = list(map(lambda x: kh(f'{ss}-{x}'), range(128)))
print('Part 1:', sum(map(lambda x: x.count('1'), m)))

cc = 0
vis = {}
def rec(x, y):
    if 0 <= x < 128 and 0 <= y < 128 and (x, y) not in vis and m[x][y] == '1':
        vis[(x, y)] = True
        for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            rec(x + dx, y + dy)
for i in range(128):
    for j in range(128):
        if m[i][j] == '1' and (i, j) not in vis:
            cc += 1
            rec(i, j)
print('Part 2:', cc)