import sys
from copy import deepcopy

particles = []
for line in sys.stdin:
    p, v, a = line.split()
    temp = [len(particles)]
    for d in [p, v, a]:
        d = d[3:d.find('>')]
        d = map(int, d.split(','))
        temp.extend(d)
    particles.append(temp)

def simulate(particles):
    for _ in range(500):
        for i, px, py, pz, vx, vy, vz, ax, ay, az in particles:
            vx += ax
            vy += ay
            vz += az
            px += vx
            py += vy
            pz += vz
            particles[i] = [i, px, py, pz, vx, vy, vz, ax, ay, az]
    return min(particles, key=lambda x: sum(i**2 for i in x[1:4]))[0]

def simulate2(particles):
    for _ in range(500):
        seen = {}
        for i in range(len(particles)):
            _, px, py, pz, vx, vy, vz, ax, ay, az = particles[i]
            vx += ax
            vy += ay
            vz += az
            px += vx
            py += vy
            pz += vz
            particles[i] = [_, px, py, pz, vx, vy, vz, ax, ay, az]
            seen[(px, py, pz)] = seen.get((px, py, pz), 0) + 1
        new_particles = []
        for part in particles:
            _, px, py, pz, *_ = part
            if seen[(px, py, pz)] < 2:
                new_particles.append(part.copy())
        particles.clear()
        particles.extend(new_particles)
    return len(particles)
print('Part 1:', simulate(deepcopy(particles)))
print('Part 2:', simulate2(deepcopy(particles)))