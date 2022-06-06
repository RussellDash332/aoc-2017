cmds = input().split(',')

def simulate(prog):
    for cmd in cmds:
        if cmd[0] == 's':
            x = int(cmd[1:])
            prog = prog[-x:] + prog[:-x]
        elif cmd[0] == 'x':
            a, b = map(int, cmd[1:].split('/'))
            prog[a], prog[b] = prog[b], prog[a]
        elif cmd[0] == 'p':
            a, b = cmd[1:].split('/')
            pa, pb = prog.index(a), prog.index(b)
            prog[pa], prog[pb] = prog[pb], prog[pa]
    return prog

prog = list('abcdefghijklmnop')
seen = [prog.copy()]
prog = simulate(prog)
print('Part 1:', ''.join(prog))

while prog not in seen:
    seen.append(prog.copy())
    prog = simulate(prog)
print('Part 2:', ''.join(seen[10**9 % len(seen)]))