SIZE = 256
ss = input()
lst = list(map(int, ss.split(',')))

cl = list(range(SIZE))
curr = 0
skip = 0
for length in lst:
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
print('Part 1:', cl[0] * cl[1])

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
print('Part 2:', ''.join(xors))