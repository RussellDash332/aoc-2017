import sys, string
from copy import deepcopy

letters = string.ascii_lowercase

cmd = []
for line in sys.stdin:
    cmd.append(line.strip().split())

def simulate(cmd):
    reg, pos = {}, 0
    rcv = None # recovered sound
    for k in letters:
        reg[k] = 0
    while pos < len(cmd):
        c = cmd[pos]
        if c[0] == 'snd':
            if c[1] in reg:
                rcv = reg[c[1]]
            else:
                rcv = int(c[1])
            pos += 1
        elif c[0] == 'set':
            if c[2] in reg:
                reg[c[1]] = reg[c[2]]
            else:
                reg[c[1]] = int(c[2])
            pos += 1
        elif c[0] == 'mul':
            if c[2] in reg:
                reg[c[1]] *= reg[c[2]]
            else:
                reg[c[1]] *= int(c[2])
            pos += 1
        elif c[0] == 'add':
            if c[2] in reg:
                reg[c[1]] += reg[c[2]]
            else:
                reg[c[1]] += int(c[2])
            pos += 1
        elif c[0] == 'mod':
            if c[2] in reg:
                reg[c[1]] %= reg[c[2]]
            else:
                reg[c[1]] %= int(c[2])
            pos += 1
        elif c[0] == 'jgz':
            if c[1] not in reg:
                check = int(c[1])
            else:
                check = reg[c[1]]
            if check > 0:
                if c[2] in reg:
                    pos += reg[c[2]]
                else:
                    pos += int(c[2])
            else:
                pos += 1
        else:
            return rcv

from collections import deque
def simulate2(cmd):
    r, r2, p, p2 = {}, {}, [0], [0]
    rcv, rcv2 = deque([]), deque([])
    for k in letters:
        r[k] = r2[k] = 0
    r2['p'] = 1
    lock = [0, 0]

    send1 = 0
    while True:
        for reg, pos, own, other, count_it in [[r, p, rcv, rcv2, False], [r2, p2, rcv2, rcv, True]]:
            while pos[0] < len(cmd):
                c = cmd[pos[0]]
                if c[0] == 'snd':
                    if c[1] in reg:
                        other.append(reg[c[1]])
                    else:
                        other.append(int(c[1]))
                    pos[0] += 1
                    send1 += count_it
                    lock[1 - int(count_it)] = 0
                elif c[0] == 'set':
                    if c[2] in reg:
                        reg[c[1]] = reg[c[2]]
                    else:
                        reg[c[1]] = int(c[2])
                    pos[0] += 1
                elif c[0] == 'mul':
                    if c[2] in reg:
                        reg[c[1]] *= reg[c[2]]
                    else:
                        reg[c[1]] *= int(c[2])
                    pos[0] += 1
                elif c[0] == 'add':
                    if c[2] in reg:
                        reg[c[1]] += reg[c[2]]
                    else:
                        reg[c[1]] += int(c[2])
                    pos[0] += 1
                elif c[0] == 'mod':
                    if c[2] in reg:
                        reg[c[1]] %= reg[c[2]]
                    else:
                        reg[c[1]] %= int(c[2])
                    pos[0] += 1
                elif c[0] == 'jgz':
                    if c[1] not in reg:
                        check = int(c[1])
                    else:
                        check = reg[c[1]]
                    if check > 0:
                        if c[2] in reg:
                            pos[0] += reg[c[2]]
                        else:
                            pos[0] += int(c[2])
                    else:
                        pos[0] += 1
                else: # rcv
                    if own:
                        reg[c[1]] = own.popleft()
                        pos[0] += 1
                    else:
                        lock[int(count_it)] = 1
                        if sum(lock) == 2:
                            return send1
                        break

print('Part 1:', simulate(deepcopy(cmd)))
print('Part 2:', simulate2(deepcopy(cmd)))