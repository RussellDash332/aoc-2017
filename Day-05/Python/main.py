import sys

arr = []
for line in sys.stdin:
    arr.append(int(line))
arr2 = arr.copy()

pos = 0
it = 0
while pos < len(arr):
    arr[pos] += 1
    pos += arr[pos] - 1
    it += 1
print('Part 1:', it)

pos = 0
it = 0
while pos < len(arr2):
    if arr2[pos] < 3:
        arr2[pos] += 1
        pos += arr2[pos] - 1
    else:
        arr2[pos] -= 1
        pos += arr2[pos] + 1
    it += 1
print('Part 2:', it)