import sys

def sorted_set(x):
    return tuple(sorted(set(x)))

valid, valid2 = 0, 0
for line in sys.stdin:
    line = line.strip().split()
    line2 = list(map(sorted_set, line))
    valid += int(len(line) == len(set(line)))
    valid2 += int(len(line2) == len(set(line2)))

print('Part 1:', valid)
print('Part 2:', valid2)