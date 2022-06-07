spin = int(input())

class Node:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class CLL:
    def __init__(self):
        self.tail = None
        self.size = 0

    def insert_at(self, node, at):
        prev, curr, succ = at, node, at.next
        prev.next, curr.prev, curr.next, succ.prev = curr, prev, succ, curr
        if self.tail == prev:
            self.tail = curr
        self.size += 1

buffer = CLL()
pos = Node(0)
pos.next, pos.prev = pos, pos
zero = pos # for Part 2
buffer.tail, buffer.size = pos, 1

for _ in range(2017):
    node = Node(buffer.size)
    for _ in range(spin + 1):
        pos = pos.next
    buffer.insert_at(node, pos)

print('Part 1:', node.next.val)

for i in range(2017, 50000000):
    node = Node(buffer.size)
    for _ in range(spin + 1):
        pos = pos.next
    buffer.insert_at(node, pos)

print('Part 2:', zero.next.val)