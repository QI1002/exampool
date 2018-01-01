
#407. Trapping Rain Water II 

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

def trapRain(data):
    
    s = stack()
    rowc, colc = len(data), len(data[0])
    mask = copy.deepcopy(data)
    max = data[0][0]
    for i in range(rowc):
        for j in range(colc):
            mask[i][j] = 0
            if (data[i][j] > max): max = data[i][j]

    seg = [ None ]
    segv = [ None ]
    lmv = [ None ]
    mg = 0
    for i in range(rowc):
        for j in range(colc):
            if (mask[i][j] != 0): continue 
            mg += 1
            segv.append(data[i][j])
            lmv.append(max)
            seg.append([])
            s.push((i,j))
            while(not s.isEmpty()):
                i, j = s.pop()
                if (mask[i][j] != 0): continue
                mask[i][j] = mg
                seg[mg].append((i,j))
                d = data[i][j]
                if (i != 0):
                    if (data[i-1][j] == d): s.push((i-1,j))
                    if (data[i-1][j] > d and data[i-1][j] < lmv[mg]): lmv[mg] = data[i-1][j]                 
                if (i != (rowc-1)):
                    if (data[i+1][j] == d): s.push((i+1,j)) 
                    if (data[i+1][j] > d and data[i+1][j] < lmv[mg]): lmv[mg] = data[i+1][j]                
                if (j != 0): 
                    if (data[i][j-1] == d): s.push((i,j-1)) 
                    if (data[i][j-1] > d and data[i][j-1] < lmv[mg]): lmv[mg] = data[i][j-1] 
                if (j != (colc-1)):
                    if (data[i][j+1] == d): s.push((i,j+1))
                    if (data[i][j+1] > d and data[i][j+1] < lmv[mg]): lmv[mg] = data[i][j+1]                
                    
    print(mask)
    print(seg)
    print(segv)
    print((max, lmv))

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
    lmu = [ i for i in range(len(segv)) ]
    lmvv = list(lmv)
    for t in order:
        d = segv[t]
        union = [t]
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
                if (not m in union): union.append(m) 
                if (lmf[m] == False or lmvv[m] < d): 
                    lmf[t] = False  
                    break              
            if (i != (rowc-1) and data[i+1][j] < d):
                m = mask[i+1][j]
                if (not m in union): union.append(m) 
                if (lmf[m] == False or lmvv[m] < d): 
                    lmf[t] = False  
                    break              
            if (j != 0 and data[i][j-1] < d):
                m = mask[i][j-1]
                if (not m in union): union.append(m) 
                if (lmf[m] == False or lmvv[m] < d): 
                    lmf[t] = False  
                    break              
            if (j != (colc-1) and data[i][j+1] < d): 
                m = mask[i][j+1]
                if (not m in union): union.append(m) 
                if (lmf[m] == False or lmvv[m] < d): 
                    lmf[t] = False  
                    break
 
        if (lmf[t] == False): continue

        min = union[0]
        maxv = lmv[t]
        for k in range(1, len(union), 1):
           uk = union[k] 
           if (min > uk): min = uk
           if (maxv < lmv[uk]): maxv = lmv[uk]
        for k in union: lmu[k], lmvv[k] = min, maxv 
        print((union, lmvv))        
        
    print(lmf)
    print(lmu)
    print(lmvv)

    vol = 0
    for i in range(rowc):
        for j in range(colc):
            m = mask[i][j]
            if (lmf[m] == False): continue 
            if (lmvv[m] < data[i][j]): raise ValueError("Wrong Calculation")
            vol += (lmvv[m]-data[i][j])
    return vol
 
grid1 = [ [ 4, 4, 4, 4, 4], 
          [ 4, 1, 2, 1, 4],
          [ 4, 1, 4, 1, 4],
          [ 4, 1, 2, 1, 4], 
          [ 4, 4, 4, 4, 4] ]

print(trapRain(grid1)) #22

grid2 = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

#print(trapRain(grid2)) #4

grid3 = [
  [1,4,3,2,3,2],
  [4,3,1,1,2,4],
  [2,4,3,2,3,1]
]

#print(trapRain(grid3)) #2

grid4 = [
  [1,4,3,2,3,2],
  [4,3,1,1,0,4],
  [2,4,3,2,1,1]
]

#print(trapRain(grid4)) #0

grid5 = [
  [1,4,3,2,3,2],
  [4,1,1,1,1,4],
  [2,4,3,2,1,1]
]

#print(trapRain(grid5)) #0

 
