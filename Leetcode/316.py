
#316. Remove Duplicate Letters

def betterRemove(s):
    h = [ [] for i in range(26) ]
    m = [ -1 for i in range(26) ]    
    for i in range(len(s)):
        oo = ord(s[i]) - ord('a')
        h[oo].append(i)
        
    print(h)
    
    for i in range(26):
        if (len(h[i]) == 0): 
            m[i] = 0  # dummy
            continue
        if (len(h[i]) == 1):
            m[i] = h[i][0]
            
    for i in range(26):        
        if (m[i] >= 0): continue        
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

"""
    a   b
      d   e
   ca d b e   5
    acd b e   1 
    a dcb e   4
    a d bce   2
    a d b ec  3 

    b   a
      e   d
   cb e a d   5
    bce a d   1 
    b eca d   4
    b e acd   2
    b e a dc  3 

    d   e
      a   b   
   cd a e b   1
    dca e b   5
    d ace b   2
    d a ecb   4
    d a e bc  3

    e   d
      b   a   
   ce b d a   1 
    ecb d a   5
    e bcd a   2
    e b dca   4
    e b d ac  3
       
    a b d e  
   ca b d e   5
    acb d e   4 
    a bcd e   1 
    a b dce   2
    a b d ec  3        

    b a e d  
   cb a e d   5
    bca e d   4 
    b ace d   1 
    b a ecd   2
    b a e dc  3        

    d e a b  
   cd e a b   1 
    dce a b   2
    d eca b   5
    d e acb   4
    d e a bc  3
             
    e d b a  
   ce d b a   1 
    ecd b a   2
    e dcb a   5
    e d bca   4
    e d b ac  3
             
"""    
    
                  