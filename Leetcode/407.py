
import copy
class stack:
    def __init__(self):
        self.body = []

    def push(self, data):
        self.body.append(data)

    def pop(self):
        if (len(self.body) == 0):
            return None
        else:
            return self.body.pop()

    def isEmpty(self):
        return True if len(self.body) == 0 else False

def localmin(data):
    
    s = stack()
    rowc, colc = len(data), len(data[0])
    mask = copy.deepcopy(data)

    for i in range(rowc):
        for j in range(colc):
            mask[i][j] = 0

    seg = [ None ]
    segv = [ None ]
    mg = 0
    for i in range(rowc):
        for j in range(colc):
            if (mask[i][j] != 0): continue 
            mg += 1
            segv.append(data[i][j])
            seg.append([])
            s.push((i,j))
            while(not s.isEmpty()):
                i, j = s.pop()
                if (mask[i][j] != 0): continue
                mask[i][j] = mg
                seg[mg].append((i,j))
                d = data[i][j]
                if (i != 0 and data[i-1][j] == d): s.push((i-1,j))                
                if (i != (rowc-1) and data[i+1][j] == d): s.push((i+1,j))               
                if (j != 0 and data[i][j-1] == d): s.push((i,j-1))               
                if (j != (colc-1) and data[i][j+1] == d): s.push((i,j+1))                
                    
    print(mask)
    print(seg)
    print(segv)

    process = [ 0 for i in range(len(segv)) ]
    order = []
    while(True):
        found = -1
        for i in range(1, len(segv), 1):
            if (process[i] == 1): continue
            if (found == -1 or segv[i] < segv[found]): 
                found = i     
        if (found == -1): break  
        process[found] = 1
        order.append(found)
   
    print(order) 
        
    lmf = [ None for i in range(len(segv)) ]
    for t in order:
        d = segv[t]
        lmf[t] = True
        for i, j in seg[t]:
            if (i == 0 or i == (rowc-1)): 
                lmf[t] = False
                break
            if (j == 0 or j == (colc-1)): 
                lmf[t] = False
                break
            if (i != 0 and data[i-1][j] < d):                
                m = mask[i-1][j]
                if (lmf[m] == False): 
                    lmf[t] = False  
                    break              
            if (i != (rowc-1) and data[i+1][j] < d):
                m = mask[i+1][j]
                if (lmf[m] == False): 
                    lmf[t] = False  
                    break              
            if (j != 0 and data[i][j-1] < d):
                m = mask[i][j-1]
                if (lmf[m] == False): 
                    lmf[t] = False  
                    break              
            if (j != (colc-1) and data[i][j+1] < d): 
                m = mask[i][j+1]
                if (lmf[m] == False): 
                    lmf[t] = False  
                    break              

    print(lmf)

    for i in range(rowc):
        for j in range(colc):
            m = mask[i][j]
            mask[i][j] = lmf[m] 

    print(mask)
 
grid = [ [ 3, 3, 3, 3, 3], 
         [ 3, 1, 2, 1, 3],
         [ 3, 1, 4, 1, 3],
         [ 3, 1, 2, 1, 3], 
         [ 3, 3, 3, 3, 3] ]

localmin(grid) 
