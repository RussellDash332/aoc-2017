import sys

cs, cs2 = 0, 0
for line in sys.stdin:
    line = list(map(int, line.split()))
    cs += max(line) - min(line)
    for i in line:
        for j in line:
            if i % j == 0 and i != j:
                cs2 += i // j
print('Part 1:', cs)
print('Part 2:', cs2)