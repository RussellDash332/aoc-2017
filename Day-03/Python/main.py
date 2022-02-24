def spiral(n):
    posx, posy = 0, 0
    dirx, diry = 1, 0
    inc = 1
    while n != 1:
        for _ in range(2):
            temp = inc
            while temp != 0:
                temp -= 1
                n -= 1
                posx += dirx
                posy += diry
                if n == 1:
                    return (posx, posy)
            dirx, diry = -diry, dirx
        inc += 1
    return (posx, posy)

def spiral2(n):
    if n == 1:
        return 1
    posx, posy = 0, 0
    dirx, diry = 1, 0
    m = {(0, 0): 1}
    inc = 1
    while True:
        for _ in range(2):
            temp = inc
            while temp != 0:
                temp -= 1
                n -= 1
                posx += dirx
                posy += diry
                check = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if abs(dx) + abs(dy) != 0 and (posx + dx, posy + dy) in m:
                            check += m[(posx + dx, posy + dy)]
                if check > n:
                    return check
                m[(posx, posy)] = check
            dirx, diry = -diry, dirx
        inc += 1

n = int(input())
x, y = spiral(n)
print('Part 1:', abs(x) + abs(y))
print('Part 2:', spiral2(n))