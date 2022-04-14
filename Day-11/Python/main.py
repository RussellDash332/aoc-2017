moves = input().split(',')
x, ys3 = 0, 0
hist = [(0, 0)]
xlim, ylim = 0, 0
for move in moves:
    if move == 'n':
        ys3 += 2
    elif move == 's':
        ys3 -= 2
    elif move == 'nw':
        x -= 2
        ys3 += 1
    elif move == 'sw':
        x -= 2
        ys3 -= 1
    elif move == 'se':
        x += 2
        ys3 -= 1
    elif move == 'ne':
        x += 2
        ys3 += 1
    hist.append((x, ys3))
    xlim = max(xlim, abs(x))
    ylim = max(ylim, abs(ys3))

from collections import deque
q = deque([(0, 0, 0)])
visited = {(0, 0)}
D = {(0, 0): 0}
while q:
    xu, ys3u, d = q.popleft()
    if xu == x and ys3u == ys3:
        print('Part 1:', d)
    for dx, dys3 in ((0, 2), (0, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)):
        if abs(xu + dx) <= xlim + 5 and abs(ys3u + dys3) <= ylim + 5 and (xu + dx, ys3u + dys3) not in visited:
            visited.add((xu + dx, ys3u + dys3))
            q.append((xu + dx, ys3u + dys3, d + 1))
            D[(xu + dx, ys3u + dys3)] = d + 1
print('Part 2:', max(map(D.get, hist)))