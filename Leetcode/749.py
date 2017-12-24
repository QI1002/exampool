
#749. Contain Virus

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

def join(l, ll):
    if not ll in l: l.append(ll)

def neighbor(seg, data, wx, wy, rowc, colc, ar, build = False, infect = False):
    result = []
    wxb = []
    wyb = []
    for y, x in seg:
        if (y > 0 and data[y-1][x] == ar and wy[y-1][x] == 0): 
            join(result, (y-1, x))
            join(wyb, (y-1, x))
        if (y < (rowc-1) and data[y+1][x] == ar and wy[y][x] == 0):
            join(result, (y+1, x))
            join(wyb, (y, x))
        if (x > 0 and data[y][x-1] == ar and wx[y][x-1] == 0):
            join(result, (y, x-1))
            join(wxb, (y, x-1))
        if (x < (colc-1) and data[y][x+1] == ar and wx[y][x] == 0):
            join(result, (y, x+1))
            join(wxb, (y, x))

    if (build):
        for y, x in wxb: wx[y][x] = 1
        for y, x in wyb: wy[y][x] = 1 

    return result
    
def wall(grid, wx, wy, rowc, colc):

    data = copy.deepcopy(grid)
    seg = [ [], [] ]
    s = stack()

    while(True):

        seed = None 
        for i in range(rowc):
            for j in range(colc):
                if (seed == None and data[i][j] == 1):
                    seed = (i, j)
                    break       
            if (seed != None): break

        #print(seed)
        if (seed == None): break

        tag = len(seg)
        seg.append([])
        s.push(seed)
        while(not s.isEmpty()):
            y, x = s.pop()
            if (y, x) in seg[tag]: continue
            seg[tag].append((y, x))
            data[y][x] = tag
            n = neighbor([(y,x)], data, wx, wy, rowc, colc, 1) 
            for nn in n: s.push(nn)

    if (len(seg) == 2): return -1, None 
    #print(seg)   

    ms = max = 0
    for k in range(2, len(seg), 1):
        n = neighbor(seg[k], data, wx, wy, rowc, colc, 0)
        if (len(n) > max): ms, max = k, len(n) 
    
    neighbor(seg[ms], data, wx, wy, rowc, colc, 0, True)
    #print((ms, seg))
    return ms, seg

def wallall(grid):

    colc = len(grid[0])
    rowc = len(grid)
    row1 = [ 0 for i in range(colc-1) ]
    row2 = [ 0 for i in range(colc) ]
    wx = [ list(row1) for i in range(rowc) ]
    wy = [ list(row2) for i in range(rowc-1) ]

    while(True):
        ms, seg = wall(grid, wx, wy, rowc, colc)        
        if (seg == None): break
        for y, x in seg[ms]: grid[y][x] = -1
        seg.pop(ms)        
        for s in seg:
            n = neighbor(s, grid, wx, wy, rowc, colc, 0)
            for y, x in n: grid[y][x] = 1
        #print((wx,wy)) 

    count = 0
    for i in range(rowc):
        for j in range(colc-1):    
            if (wx[i][j] == 1): count += 1

    for i in range(rowc-1):
        for j in range(colc):    
            if (wy[i][j] == 1): count += 1

    return count

grid1 = [[0,1,0,0,0,0,0,1],
         [0,1,0,0,0,0,0,1],
         [0,0,0,0,0,0,0,1],
         [0,0,0,0,0,0,0,0]]

print(wallall(grid1))

grid2 = [[1,1,1],
         [1,0,1],
         [1,1,1]]

print(wallall(grid2))

grid3 = [[1,1,1,0,0,0,0,0,0],
         [1,0,1,0,1,1,1,1,1],
         [1,1,1,0,0,0,0,0,0]]

print(wallall(grid3))

grid4 = [[0,0,0,0,0,0,0,0,0],
         [0,1,1,0,1,1,0,1,1],
         [0,0,0,0,0,0,0,0,0]]

print(wallall(grid4))

