import sys

m = {}
i = 0
for line in sys.stdin:
    line = line.strip()
    for j in range(len(line)):
        m[(i, j)] = line[j]
    i += 1
m2 = m.copy()

def turn_left():
    global dr, dc
    dr, dc = -dc, dr

def turn_right():
    global dr, dc
    dr, dc = dc, -dr

def move():
    global r, c, dr, dc
    r += dr
    c += dc

r, c, dr, dc = i // 2, j // 2, -1, 0 # facing up
infection = 0
for _ in range(10000):
    if (r, c) not in m:
        m[(r, c)] = '.'
    if m[(r, c)] == '#':
        turn_right()
        m[(r, c)] = '.'
    else:
        turn_left()
        m[(r, c)] = '#'
        infection += 1
    move()

print('Part 1:', infection)

r, c, dr, dc = i // 2, j // 2, -1, 0 # facing up
infection = 0
m = m2
for _ in range(10000000):
    if (r, c) not in m:
        m[(r, c)] = '.'
    if m[(r, c)] == '#':
        turn_right()
        m[(r, c)] = 'F'
    elif m[(r, c)] == 'F':
        turn_right()
        turn_right()
        m[(r, c)] = '.'
    elif m[(r, c)] == '.':
        turn_left()
        m[(r, c)] = 'W'
    else:
        m[(r, c)] = '#'
        infection += 1
    move()

print('Part 2:', infection)