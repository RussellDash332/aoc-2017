s = input().replace('{', '[').replace('}', ']')
new = []
balance = 0
cont = False
count_it = False
garbage = 0
for k in s:
    if k == '!' and not cont:
        cont = True
        continue
    if cont:
        cont = False
        continue
    if k == '<':
        if not count_it:
            count_it = True
            balance = 1
            continue
        balance = 1
    elif k == '>':
        if count_it:
            count_it = False
        else:
            garbage += 1
        balance = 0
        continue
    if balance == 0:
        new.append(k)
    else:
        garbage += 1
tree = ''.join(new)
while True:
    new_tree = tree.replace('[,', '[')
    if new_tree == tree:
        break
    tree = new_tree
tree = eval(tree)

def score(t):
    def helper(subt, d):
        if not subt:
            return d
        return d + sum(helper(i, d + 1) for i in subt)
    return helper(t, 1)

print('Part 1:', score(tree))
print('Part 2:', garbage)