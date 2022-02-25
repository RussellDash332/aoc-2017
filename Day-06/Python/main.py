arr = list(map(int, input().split()))
look = {tuple(arr): 1}

it = 1
while True:
    pos = arr.index(max(arr))
    for i in range(arr[pos]):
        arr[pos] -= 1
        arr[(pos + i + 1) % len(arr)] += 1
    if tuple(arr) in look:
        break
    it += 1
    look[tuple(arr)] = it
print('Part 1:', it)
print('Part 2:', it - look[tuple(arr)] + 1)