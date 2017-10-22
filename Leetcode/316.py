
#316. Remove Duplicate Letters

def betterRemove(s):
    h = [ [] for i in range(26) ]    
    for i in range(len(s)):
        oo = ord(s[i]) - ord('a')
        h[oo].append(i)
        
    print(h)
    
    end = -1
    m = []
    for i in range(26):
        if (len(h[i]) == 0): continue
        if (len(h[i]) == 1):
            m.append(h[i][0])        
            if (end < i): end = i
        else:
            start = h[i][0]
            for j in range(0, len(h[i]), 1):
                if (h[i][j] > end):
                    start = h[i][j]
            m.append(start)
    
    print(m)
    ms = sorted(m)        
    mm = [ s[i] for i in ms ]        
    return "".join(mm)                 
                
sample = "bcabc"    
print(betterRemove(sample))

sample = "cbacdcbc"    
print(betterRemove(sample))
        