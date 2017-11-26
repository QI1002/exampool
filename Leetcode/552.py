
#552. Student Attendance Record II
 
import math 

#0: attend 1: late 2: absent
def checkRect(r):
    d = {0:0, 1:0, 2:0}
    for x in r: d[x]+= 1    
    return (d[1] <= 2 and d[2] <= 1)
        
def attendRec(k):
    count = int(math.pow(3, k))
    c = 0
    cc = [ 0 for i in range(k+1) ]
    result = [] 
    while(c < count):
        if (checkRect(cc)): result.append(list(cc[0:k]))  
        c += 1              
        i = 0        
        while(True):
            cc[i] += 1
            if (cc[i] < 3): break 
            cc[i] = 0
            i += 1
            
    return sorted(result)        

def attendRec2(k):
    pattern1 = [[1],[2]]
    pattern2 = [[1,1],[2,1],[1,2]]
    pattern3 = [[1,1,1],[2,1,1],[1,2,1],[1,1,2]]
    t = [ 0 for i in range(k) ]
    result = [t]
    
    for x in range(k):
        for n in range(len(pattern1)):
            tt = list(t)
            tt[x] = pattern1[n][0]
            result.append(tt)
            
    for x in range(k):
        for y in range(x+1, k, 1):
            for n in range(len(pattern2)):
                tt = list(t)
                tt[x] = pattern2[n][0]
                tt[y] = pattern2[n][1]
                result.append(tt)
                
    for x in range(k):
        for y in range(x+1, k, 1):
            for z in range(y+1, k, 1):
                for n in range(len(pattern3)):
                    tt = list(t)
                    tt[x] = pattern3[n][0]
                    tt[y] = pattern3[n][1]
                    tt[z] = pattern3[n][2]
                    result.append(tt)
                
    return sorted(result)
    
for i in range(10):    
    r1 = attendRec(2)
    r2 = attendRec2(2)
    if (r1 != r2): print((i, r1, r2))