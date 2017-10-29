
#330. Patching Array

def patch(data, n):
    tm = sorted(data)
    r = []
    m = n
    tl = []
    
    if (tm[0] == 1):
        tl.append(tm[0])
        tm.pop(0)
        while(tm[0] <= (2* tl[-1])):
            tl.append(tm.pop(0))                 
    
    ss = sum(tl)
    
    while(len(tm) != 0):    
        max = tm.pop()
        m -= max
     
    print((m, ss, tl, tm)) 
    while(m > 2):
        h = m // 2
        r.append(h)
        m -= h
    r.append(r)
               
    return r
    
nums, n = [1,3], 6
print("{0}, {1} => {2}".format(nums, n, patch(nums, n)))            
            