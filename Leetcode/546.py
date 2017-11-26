
#546. Remove Boxes

def score(data):
    seg = []
    start = 0
    for i in range(1,len(data),1):
        if (data[i-1] != data[i]):
            seg.append([start, i-1])
            start = i
            
    seg.append([start, len(data)-1])
    
    if (len(seg) == 1): 
        return len(data)*len(data), [data]
        
    max = 0
    maxr = None
    for i in range(len(seg)):
        ss = (seg[i][1]-seg[i][0]+1)*(seg[i][1]-seg[i][0]+1)
        l = data[:seg[i][0]]
        l.extend(data[seg[i][1]+1:])        
        s, r = score(l)
        if ((s+ss) > max): 
           max = s+ss
           r.insert(0, data)
           maxr = r
           
    return max, maxr
              
print(score([1, 3, 2, 2, 2, 3, 4, 3, 1]))    
#print(score([1, 1, 1, 1]))
#print(score([1, 2, 3, 2]))
            