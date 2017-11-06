
#440. K-th Smallest in Lexicographical Order

def numFirst(n, k):
    result = []
    digits = 0
    bound = 1
    while(bound <= n):
        result.append(bound)
        digits += 1
        bound *= 10
        
    bound //= 10
    f = n//bound
    s = n - f*bound
    
    if (f < k): result.pop()
    else:
        if (f == k): result[-1] = (s+1)
    
    #print((f,s,k,result))
    return result    
    
def smallOrder(n, k):
    k -= 1
    lower = 0
    for i in range(1, 10, 1):
        r = numFirst(n, i)
        upper = lower + sum(r)
        if (k >= lower and k < upper):
            v = i
            for j in range(len(r)):
                upper = lower + r[j]
                if (k >= lower and k < upper): 
                    return v + (k - lower)
                lower = upper
                v *= 10
        lower = upper
        
    return None

r = []
for i in range(1, 101, 1):
    r.append(str(i))
    r = sorted(r)
    for j in range(i):
        c1 = smallOrder(i, j+1)
        c2 = int(r[j])
        if (c1 != c2): print((i, j, c1, c2))