import sys

reg = {}
mmax = 0
for line in sys.stdin:
    what, do, much, when, what2, rel, how = line.strip().split()
    if what not in reg:
        reg[what] = 0
    if what2 not in reg:
        reg[what2] = 0
    if eval(f'reg["{what2}"]{rel}{how}'):
        cmd = f'reg["{what}"]{do}{much}'.replace('inc', '+=').replace('dec', '-=')
        exec(cmd)
    mmax = max(max(reg.values()), mmax)
print('Part 1:', max(reg.values()))
print('Part 2:', mmax)