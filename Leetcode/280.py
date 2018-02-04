
#280. Wiggle Sort

def isWiggle(data):
    for i in range(1, len(data), 2):
        p = data[i-1]
        c = data[i]
        n = data[i+1] if (i+1) < len(data) else c
        if (not (p <= c or c >= n)):
            return False

    return True    

def swap(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp

def wiggle(data):
    data = list(data)
    for i in range(1, len(data), 2):
        p = data[i-1]
        c = data[i]
        if (p > c): swap(data, i-1, i)
        if ((i+1) >= len(data)): break
        n = data[i+1]
        c = data[i]
        if (n >c): swap(data, i+1, i)

    return data, isWiggle(data)

def permutation(n):
    if (n == 0): return [[]]
    result = []
    t = permutation(n-1)
    for tt in t:
        for i in range(len(tt)+1):
            tp = list(tt)
            tp.insert(i, n)
            result.append(tp)

    return result        
        
data = [3,5,2,1,6,4]
print("{0}=>{1}".format(data, wiggle(data)))
t = permutation(len(data))
for tt in t:
    print("{0}=>{1}".format(data, wiggle(tt)))
    
