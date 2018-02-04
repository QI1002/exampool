
#277. Find the Celebrity

import random
def celebrity(n, data):
    know = [ 0 for i in range(n) ]
    isknown = [ 0 for i in range(n) ]
    for d in data:
        a = d[0]
        b = d[1]
        if (a == b): raise ValueError("the same couple")
        know[a] += 1
        isknown[b] += 1

    for i in range(n):
        if (know[i] == 0 and isknown[i] == (n-1)):
            return i 

    return -1

n = 10
t = random.randint(0, n-1)
data = []
for i in range(n*2):
    a = random.randint(0, n-1)
    b = random.randint(0, n-1)
    if (a == b): continue
    if (a == t): continue
    if (not (a, b) in data):
        data.append((a, b))

print(t)
for i in range(n):
    if (i == t): continue
    if (not (i, t) in data):
        data.append((i, t))

tt = celebrity(n, data)
print("{0}:{1}".format(t, tt))
if (t != tt): print(data)

