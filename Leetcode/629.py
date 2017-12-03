
#629. K Inverse Pairs Array 

def kInvPairs(n, k):
    if (n == 1): 
        return [[1]] if (k == 0) else []
    
    result = []
    for i in range(k+1):
        r = kInvPairs(n-1, i)
        for x in r:
            l = list(x)
            if (len(x) >= (k-i)):
                l.insert(len(x)-k+i, n)    
                result.append(l) 
                
    return result
    
def numPairs(n):
    return n*(n-1)//2
        
s = 0        
n = 6
nn = numPairs(n)        
for i in range(nn+1):
   pp = kInvPairs(n, i)
   print("{0}:{1}:{2}".format(i, len(pp), pp))    
   s += len(pp)
print("sum of all is {0}".format(s))   