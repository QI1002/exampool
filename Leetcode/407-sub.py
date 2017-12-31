
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

    def empty(self):
        self.body = []

    def isEmpty(self):
        return True if len(self.body) == 0 else False

def localmin2(data):

    s = stack()
    rowc, colc = len(data), len(data[0])
    mask = copy.deepcopy(data)

    for i in range(rowc):
        for j in range(colc):
            mask[i][j] = 0

    for i in range(rowc): mask[i][0] = mask[i][colc-1] = -1
    for j in range(1,colc-1): mask[0][j] = mask[rowc-1][j] = -1

    for i in range(1, rowc-1):
        for j in range(1, colc-1):
            s.push((i,j))
            lm_flag = True
            lm = []
            while(not s.isEmpty()):
                i, j = s.pop()
                if (data[i-1][j] < d or data[i+1][j] < d or
                    data[i][j-1] < d or data[i][j+1] < d):
                    lm_flag = False
                lm.append((i,j))
                d = data[i][j]
                if (data[i-1][j] == d): s.push((i-1,j))                
                if (data[i+1][j] == d): s.push((i+1,j))               
                if (data[i][j-1] == d): s.push((i,j-1))               
                if (data[i][j+1] == d): s.push((i,j+1))                
                
            if (lm_flag):
                mg += 1 
                for ii,jj in lm: mask[ii][jj] = mg
            else: 
                for ii,jj in lm: mask[ii][jj] = -1                  	


def localmin(data):
    
    s = stack()
    rowc, colc = len(data), len(data[0])
    mask = copy.deepcopy(data)

    for i in range(rowc):
        for j in range(colc):
            mask[i][j] = 0

    mg = 0
    for i in range(rowc):
        for j in range(colc):
            if (mask[i][j] != 0): continue 
            mg += 1
            s.push((i,j))
            while(not s.isEmpty()):
                i, j = s.pop()
                if (mask[i][j] != 0): continue
                mask[i][j] = mg
                d = data[i][j]
                if (i != 0 and data[i-1][j] == d): s.push((i-1,j))                
                if (i != (rowc-1) and data[i+1][j] == d): s.push((i+1,j))               
                if (j != 0 and data[i][j-1] == d): s.push((i,j-1))               
                if (j != (colc-1) and data[i][j+1] == d): s.push((i,j+1))                
                    
    print(mask)
 
grid = [ [ 3, 3, 3, 3, 3], 
         [ 3, 1, 2, 1, 3],
         [ 3, 1, 2, 1, 3],
         [ 3, 1, 1, 1, 3], 
         [ 3, 3, 3, 3, 3] ]

localmin(grid) 
