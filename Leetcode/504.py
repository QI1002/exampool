
#504. IPO

def IPO(w,k,p,c):

    r = []
    for i in range(k):
        mi = -1        
        for j in range(len(c)):
            if (w >= c[j]):
                if (mi == -1 or p[mi] < p[j]): 
                    mi = j     
        
        if (mi != -1):
            w += p[mi]        
            r.append(mi)        
                
    return r, w
    
W = 0
K = 2 
Profits = [1,2,3]
Capitals = [0,1,1]
print(IPO(W,K,Profits,Capitals))
