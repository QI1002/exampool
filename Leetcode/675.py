
#675. Cut Off Trees for Golf Event

import copy
def cuttree(grid):

    data = copy.deepcopy(grid)
    colc = len(grid[0])
    rowc = len(grid)

    steps = x = y = 0
    data[x][y] = 0
    while(True):
        #print((y,x))
        nn = [] 
        if (y > 0 and data[y-1][x] != 0): nn.append((y-1,x))
        if (y < (rowc-1) and data[y+1][x] != 0): nn.append((y+1,x))
        if (x > 0 and data[y][x-1] != 0): nn.append((y,x-1))
        if (x < (colc-1) and data[y][x+1] != 0): nn.append((y,x+1))
        if (len(nn) == 0): break
        mh = 0
        for yn, xn in nn:
            if (data[yn][xn] > mh): 
                mh, x, y = data[yn][xn], xn, yn

        data[y][x] = 0  
        steps += 1

    for i in range(rowc):
        for j in range(colc):
            if (data[i][j] != 0): 
                return -1

    return steps 

grid1 = [[1,2,3],
         [0,0,4],
         [7,6,5]]

print(cuttree(grid1))

grid2 = [[1,2,3],
         [0,0,0],
         [7,6,5]]

print(cuttree(grid2))

grid3 = [[2,3,4],
         [0,0,5],
         [8,7,6]]

print(cuttree(grid3))

