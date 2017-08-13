
#return the smallest index >= v 
def search(ll, l, r, v):
    while(True):
        m = (l + r)//2
        vv = ll[m]
        print(str(l)+ " " + str(r) + " " + str(m))
        if (vv == v):
            return m  
        if (l == m):
            rr = ll[r]
            if (v == rr):
                return r
            else:                                        
                return (r+1 if (rr < v) else r) if (vv < v) else l            
        else:
            if (vv < v):            
                l = m
            else:
                r = m        

def search_old(ll, l, r, v):
    while((l+1) < r):
        m = (l + r)//2
        if (ll[m] == v):
            return m       
        if (ll[m] < v):
            l = m
        else:
            r = m
                
    if (v < ll[l]):
        return l
    if (v > ll[r]):
        return r+1
    else:
        return l+1    
        
def searchall(ll, v):
    return search(ll, 0, len(ll)-1, v)            
           
           
data = [1,4,7,10,15]
tail = [0,2,8,20]           
print("find {0} in {1} is {2}".format(0, data, searchall(data, 0)))
print("find {0} in {1} is {2}".format(2, data, searchall(data, 2)))
print("find {0} in {1} is {2}".format(5, data, searchall(data, 5)))            
print("find {0} in {1} is {2}".format(8, data, searchall(data, 8)))
print("find {0} in {1} is {2}".format(20, data, searchall(data, 20)))

def merge_tail(aa, bb):
    r = len(aa)-1
    aa.extend(bb)
    rr = len(aa)-1
    for i in range(len(bb), 0, -1):
        j = search(data, 0, r, bb[i-1])
        while(r >= j):
            aa[rr] = aa[r]
            rr -= 1
            r -= 1
        aa[rr] = bb[i-1]
        rr -= 1            
        
cc = list(data)        
merge_tail(data, tail)
print("result of {0} and {1} = {2}".format(cc,tail,data))                
    