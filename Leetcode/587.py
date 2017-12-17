
#587. Erect the Fence

def slope(t1, t2):
    if (t1[0] == t2[0]):
        return '+' if t2[1] > t1[1] else '-'
    return (t2[1]-t1[1])/(t2[0]-t1[0]) 

def sCompare(a, b):
    if (a == b): return 0
    if (a == '+'): return 1 
    if (a == '-'): return -1 
    if (b == '+'): return -1 
    if (b == '-'): return 1 
    return 1 if (a > b) else -1 

def dCompare(a,b,c):
    ab = (a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])
    ac = (a[0]-c[0])*(a[0]-c[0])+(a[1]-c[1])*(a[1]-c[1])
    if (ab == ac): return 0 
    return 1 if (ab > ac) else -1
        
def erect(t):
    result = []

    left = t[0]
    for i in range(1, len(t)):
        if (t[i][0] < left[0]):
            left = t[i]
        if (t[i][0] == left[0] and t[i][1] < left[1]):
            left = t[i]

    result.append(left)
    ns = None
    while(left != result[-1] or len(result) == 1): 
        ms = mst = None
        for i in range(len(t)):
            if (t[i] == result[-1]): continue
            s = slope(result[-1], t[i])
            print((s, result[-1], t[i]))
            if (ns == None or sCompare(ns, s) >= 0):
                if (ms == None):  
                    ms, mst = s, t[i]
                    continue
                if (sCompare(s, ms) > 0):
                    ms, mst = s, t[i]  
                if (sCompare(ms, s) == 0 and dCompare(result[-1], t[i], mst) < 0):
                    ms, mst = s, t[i] 
        print((ns, ms, mst, result))
        ns = ms
        result.append(mst)

samples = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
print(erect(samples))  
