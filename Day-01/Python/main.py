n = input()
print("Part 1:", sum(int(n[i]) for i in range(len(n)) if n[i] == n[(i + 1) % len(n)]))
print("Part 2:", sum(int(n[i]) for i in range(len(n)) if n[i] == n[(i + len(n) // 2) % len(n)]))