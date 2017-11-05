
#407. Trapping Rain Water II

def trapRain(blocks):
    colc = len(blocks[0])
    rowc = len(blocks)
    row = [ 0 for i in range(colc) ]
    m = [ list(row) for i in range(rowc) ]    
    id = 0
    max = 0
    for i in range(rowc):
        for j in range(colc):
            if (max < blocks[i][j]):  max = blocks[i][j]
    
    update = True        
    while(update):
        update = False
        for i in range(1, rowc-1, 1):
            for j in range(1, colc-1, 1):
                if (m[i][j] != 0): continue
                mark = 0
                s = blocks[i][j]
                if (blocks[i-1][j] >= s or m[i-1][j] != 0):
                    mark += 1
                if (blocks[i+1][j] >= s or m[i+1][j] != 0):
                    mark += 1
                if (blocks[i][j-1] >= s or m[i][j-1] != 0):
                    mark += 1
                if (blocks[i][j+1] >= s or m[i][j+1] != 0):
                    mark += 1
                if (mark == 4): 
                    id += 1
                    m[i][j], update = id, True
                
    print(m)

    update = True                
    while(update):
        update = False
        for i in range(1, rowc-1, 1):
            for j in range(1, colc-1, 1):
                if (m[i][j] == 0): continue
                min = m[i][j]
                if (m[i-1][j] < min and m[i-1][j] != 0):
                    min, update = m[i-1][j], True
                if (m[i+1][j] < min and m[i+1][j] != 0):
                    min, update = m[i+1][j], True
                if (m[i][j-1] < min and m[i][j-1] != 0):
                    min, update = m[i][j-1], True
                if (m[i][j+1] < min and m[i][j+1] != 0):
                    min, update = m[i][j+1], True
                if (update == False): continue       
                if (m[i-1][j] != 0): m[i-1][j] = min
                if (m[i+1][j] != 0): m[i+1][j] = min
                if (m[i][j-1] != 0): m[i][j-1] = min
                if (m[i][j+1] != 0): m[i][j+1] = min
            
    print(m)
                
    groups = {}
    bounds = {}
    for i in range(1, rowc-1, 1):
        for j in range(1, colc-1, 1):
            if (m[i][j] == 0): continue
            id = m[i][j]
            if (not id in groups): groups[id] = []
            if (not id in bounds): bounds[id] = max             
            groups[id].append((i,j))
            if (blocks[i-1][j] < bounds[id] and m[i-1][j] == 0): bounds[id] = blocks[i-1][j]
            if (blocks[i+1][j] < bounds[id] and m[i+1][j] == 0): bounds[id] = blocks[i+1][j]
            if (blocks[i][j-1] < bounds[id] and m[i][j-1] == 0): bounds[id] = blocks[i][j-1]
            if (blocks[i][j+1] < bounds[id] and m[i][j+1] == 0): bounds[id] = blocks[i][j+1]            
    
    print(groups)
    print(bounds)
    
    vols = 0
    for i in range(1, rowc-1, 1):
        for j in range(1, colc-1, 1):
            if (m[i][j] == 0): continue
            id = m[i][j]
            if (bounds[id] > blocks[i][j]):
                vols += (bounds[id] - blocks[i][j])

    return vols

blocks = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

print(trapRain(blocks))

blocks = [
  [1,4,3,2,3,2],
  [4,3,1,1,2,4],
  [2,4,3,2,3,1]
]

print(trapRain(blocks))
