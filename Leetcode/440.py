
#440. K-th Smallest in Lexicographical Order

def numFirst(n, k):
    result = []
    digits = 0
    bound = 1
    while((bound*k) <= n):
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
    v = 0
    while(v <= n):
        for i in range(10):
            if (i == 0 and v == 0): continue
            r = numFirst(n, v+i)
            upper = lower + sum(r)
            #print((v,i,r,lower,upper))
            if (k >= lower and k < upper):
                v += i
                upper = lower + r[0]
                if (upper == (lower+1) and k == lower): 
                    return v
                lower = upper
                v *= 10
                break
            lower = upper
        
    return None

#for i in range(1,1001,1):
#    print(smallOrder(1000,i))

r = []
for i in range(1, 1001, 1):
    r.append(str(i))
    r = sorted(r)
    for j in range(i):
        c1 = smallOrder(i, j+1)
        c2 = int(r[j])
        if (c1 != c2): print((i, j, c1, c2))
