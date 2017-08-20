
def search(data, l, r, v):

    while((l+1) < r):
      
        m = (l+r)//2
        vv = data[m]    
        if (vv == v):
            return m
            
        if (l == m):
            rr = data[r]
            return r if (rr == v) else None
        else: 
            if (v > vv):
                l = m 
            else:
                r = m             
    
    
def findPairs(data, datasum):
    sort = sorted(data)
    count = len(sort)
    result = []
    for i in range(count):
        item = sort[i]
        if (item > datasum//2):
            continue
        v = datasum - item
        vv = search(sort, 0, len(sort)-1, v)
        if (vv != None):
            result.append((item, v))
            
    return result
       
data = list(range(1,10,2))
data.extend(list(range(2,11,2)))
print(data)
print(findPairs(data, 10))
