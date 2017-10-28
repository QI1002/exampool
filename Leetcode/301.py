
#301 Remove Invalid Parentheses

def removeInvalidP(s):
    count = len(s)
    row = [ 0 for i in range(count) ] 
    m = [ list(row) for i in range(count) ] 
    
    for i in range(count):
        for j in range(count):
            m[i][j] = []
            
    for i in range(count):
        for j in range(count-i):
            start = j
            end = j + i 
            if (i == 0):
                m[start][end].extend([start])
            else: 
                if (i == 1):
                    if (s[start] != "(" or s[end] != ")"):
                        m[start][end].extend([start, end])
                else: 
                    if (s[start] == ")"):
                        m[start][end].extend([start])    
                        m[start][end].extend(m[start+1][end])
                    else:
                        m1, m2 = [], []
                        if (s[start+1] == ")"):
                            m1 = list(m[start+2][end])
                        else:
                            m1 = [start]                            
                            m1.extend(m[start+1][end])
                        if (s[end] == ")"):
                            m2 = list(m[start+1][end-1])
                        else:
                            m2 = list(m[start][end-1])
                            m2.extend([end])
                        
                        m[start][end] = m2 if (len(m1) > len(m2)) else m1
 
    #print(m)                      
    return m[0][count-1]
        
                        
#print(removeInvalidP("(()"))
print(removeInvalidP("()())()"))