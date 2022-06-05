a, b = int(input().split()[-1]), int(input().split()[-1])
aa, bb = a, b
GEN_A, GEN_B, MOD = 16807, 48271, 2**31 - 1

match = 0
for _ in range(4 * 10**7):
    a, b = (a * GEN_A) % MOD, (b * GEN_B) % MOD
    match += bin(a)[2:].zfill(16)[-16:] == bin(b)[2:].zfill(16)[-16:]
print('Part 1:', match)

a, b = aa, bb
match = 0
for _ in range(5 * 10**6):
    a, b = (a * GEN_A) % MOD, (b * GEN_B) % MOD
    while a % 4 != 0:
        a = (a * GEN_A) % MOD
    while b % 8 != 0:
        b = (b * GEN_B) % MOD
    match += bin(a)[2:].zfill(16)[-16:] == bin(b)[2:].zfill(16)[-16:]
print('Part 2:', match)