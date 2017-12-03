
#514. Freedom Trail 

def smallDist(s, r, c):
    min = 2*len(r)
    for i in range(len(r)):
        if (r[i] != c): continue
        if (abs(i-s) < min): 
            min = abs(i-s) 
        if ((len(r)-abs(i-s)) < min):
            min = len(r)-abs(i-s)     
            
    return min
            
def trail(s, r, k):
    if (len(k) == 1):
        return smallDist(s, r, k[0])
        
    min = 2*len(r)    
    for i in range(len(r)):
        if (r[i] != k[0]): continue
        m = trail(i, r, k[1:])
        n = abs(i-s) if (abs(i-s) <= len(r)//2) else len(r)-abs(i-s)        
        if (min > (m+n)): min = m+n
            
    return min
            
def trailbutton(r, k):
    return trail(0, r, k) + len(k)
                
rings = "godding"
keys = "gdio"    
print(trailbutton(rings, keys))

rings = "godding"
keys = "gdig"    
print(trailbutton(rings, keys))