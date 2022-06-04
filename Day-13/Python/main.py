import sys

d = {}
for line in sys.stdin:
    a, b = line.split(': ')
    d[int(a)] = int(b)

def simulate(offset):
    sev = 0
    for pos in range(max(d) + 1):
        if pos in d and (pos + offset) % (2 * (d[pos] - 1)) == 0:
            sev += pos * d[pos]
    return sev

def simulate2(offset):
    for pos in d:
        if (pos + offset) % (2 * (d[pos] - 1)) == 0:
            return False
    return True

print('Part 1:', simulate(0))
t = 1
while True:
    if simulate2(t):
        break
    t += 1
print('Part 2:', t)