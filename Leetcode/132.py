
#132. Palindrome Partitioning II

def isPal(s):
    count = len(s)//2
    for i in range(count):
        if (s[i] != s[len(s)-i-1]):
            return False
    
    return True
        
def pDivide(s):
    count = len(s)
    row = [ 0 for i in range(count) ] 
    p = [ list(row) for i in range(count) ]
    row = [ -1 for i in range(count) ] 
    d = [ list(row) for i in range(count) ]
    dd = [ list(row) for i in range(count) ]
    
    for i in range(count):
        for j in range(count-i):
            start = j
            end = j + i
            if (s[start] == s[end]): 
                if (i <= 1): p[start][end] = 1
                else: p[start][end] = p[start+1][end-1]  
    
    #print(p)
            
    for i in range(count):
        for j in range(count-i):
            start = j
            end = j + i
            if (i == 0): d[start][end] = 0
            else: 
                if (p[start][end] == 1):
                    d[start][end] = 0
                else:
                    kk = start
                    min = d[start+1][end]+1
                    for k in range(start+1, end, 1):
                        if (p[start][k] == 1):
                            v = d[k+1][end]+1
                            if (min > v): min,kk = v,k
                    d[start][end] = min                    
                    dd[start][end] = kk
    #print(d)
    
    start = 0
    end = count-1
    result = []
    while(d[start][end] != 0):
        kk = dd[start][end]
        start = kk+1
        result.append(kk)
         
    #print((d[0][count-1], result))
         
    ss = list(s)     
    for i in range(len(result)-1,-1,-1):
        ss.insert(result[i]+1, ",")
           
    return "".join(ss)
    
print(pDivide("abccbd"))        
print(pDivide("abcdbd"))    
print(pDivide("abb"))    
print(pDivide("abba"))
print(pDivide("abbacd"))
print(pDivide("palindrome"))