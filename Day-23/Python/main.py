import sys, string, time

letters = string.ascii_lowercase

cmd = []
for line in sys.stdin:
    cmd.append(line.strip().split())

def simulate():
    reg, pos, calls = {}, 0, 0
    for k in 'abcdefgh':
        reg[k] = 0
    while pos < len(cmd):
        c = cmd[pos]
        if c[0] == 'set':
            if c[2] in reg:
                reg[c[1]] = reg[c[2]]
            else:
                reg[c[1]] = int(c[2])
            pos += 1
        elif c[0] == 'sub':
            if c[2] in reg:
                reg[c[1]] -= reg[c[2]]
            else:
                reg[c[1]] -= int(c[2])
            pos += 1
        elif c[0] == 'mul':
            if c[2] in reg:
                reg[c[1]] *= reg[c[2]]
            else:
                reg[c[1]] *= int(c[2])
            pos += 1
            calls += 1
        else: # jnz
            if c[1] not in reg:
                check = int(c[1])
            else:
                check = reg[c[1]]
            if check:
                if c[2] in reg:
                    pos += reg[c[2]]
                else:
                    pos += int(c[2])
            else:
                pos += 1
    return calls

print('Part 1:', simulate())

# Part 2 shall be hardcoded here
# TLDR finding the number of composite numbers from 106500 to 123500 with step 17
h = 0
for b in range(106500, 123501, 17):
    for d in range(2, b):
        if b % d == 0:
            h += 1
            break
print('Part 2:', h)