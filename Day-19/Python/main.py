import sys

m = []
for line in sys.stdin:
    m.append(line)

for i in range(len(m[0])):
    if m[0][i] == '|':
        sr, sc = 0, i

dr, dc = 1, 0
letters = []
steps = 0
while True:
    steps += 1
    if m[sr][sc] == '|':
        if m[sr + dr][sc] in '|+' or m[sr + dr][sc].isalnum():
            sr += dr
        elif m[sr + dr][sc] == '-':
            sr += 2 * dr
            steps += 1
    elif m[sr][sc] == '-':
        if m[sr][sc + dc] in '-+' or m[sr][sc + dc].isalnum():
            sc += dc
        elif m[sr][sc + dc] == '|':
            sc += 2 * dc
            steps += 1
    elif m[sr][sc] == '+':
        if dc == 0:
            if m[sr][sc - 1].strip():
                sc -= 1
                dr, dc = 0, -1
            elif m[sr][sc + 1].strip():
                sc += 1
                dr, dc = 0, 1
        else: # dr == 0
            if m[sr - 1][sc].strip():
                sr -= 1
                dr, dc = -1, 0
            elif m[sr + 1][sc].strip():
                sr += 1
                dr, dc = 1, 0
    elif m[sr][sc].isalnum():
        letters.append(m[sr][sc])
        sr += dr
        sc += dc
        if dr == 0 and m[sr][sc] == '|':
            sc += dc
            steps += 1
        elif dc == 0 and m[sr][sc] == '-':
            sr += dr
            steps += 1
    else:
        break

print('Part 1:', ''.join(letters))
print('Part 2:', steps - 1)