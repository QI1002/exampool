
#514. Freedom Trail 

def trail(s, r, k):
    if (len(k) == 0):
        return 0
        
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
keys = "gd"    
print(trailbutton(rings, keys))
                
rings = "godding"
keys = "gdio"    
print(trailbutton(rings, keys))

rings = "godding"
keys = "gdig"    
print(trailbutton(rings, keys))