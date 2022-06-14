import sys

state = input().strip()[-2]
steps = int(input().split()[-2])

rule = {}
for line in sys.stdin:
    # dump newline
    curr = input().strip()[-2]
    rule[curr] = {}
    
    for i in range(2):
        rule[curr][i] = {}
        input() # if current value is i
        rule[curr][i]['write'] = int(input().strip()[-2])
        rule[curr][i]['move'] = input().strip().split()[-1][:-1]
        rule[curr][i]['continue'] = input().strip()[-2]

pos, tape = 0, {}
for _ in range(steps):
    if pos not in tape:
        tape[pos] = 0
    val = rule[state][tape[pos]]
    tape[pos] = val['write']
    pos += {'right': 1, 'left': -1}[val['move']]
    state = val['continue']

print('Part 1:', sum(tape.values()))
print('Part 2: THE END!')