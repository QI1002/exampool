
#85. Maximal Rectangle

def max(a, b):
    return a if (a > b) else b

def updateMax(maxArea, maxR, pos, maxr):
    #print((pos, maxr))
    area = (pos[0]-maxr[0]+1)*(pos[1]-maxr[1]+1)
    if (area > maxArea):
        maxArea = area
        maxR = pos,maxr

    return maxArea, maxR

def maxRect(matrix):
    rowc = len(matrix)
    colc = len(matrix[0])
    row = [ None for i in range(colc) ]
    maxr = [ list(row) for i in range(rowc) ]
    maxArea = 0
    maxR = None

    maxr[0][0] = (0,0) if (matrix[0][0] == 1) else None
    for i in range(1, colc, 1):
        if (matrix[0][i] == 1):
            maxr[0][i] = (0, i) 
            if (maxr[0][i-1] != None): maxr[0][i] = maxr[0][i-1]
            maxArea, maxR = updateMax(maxArea, maxR, (0,i), maxr[0][i])

    for i in range(1, rowc, 1):

        if (matrix[i][0] == 1): 
            maxr[i][0] = (i, 0)
            if (maxr[i-1][0] != None): maxr[i][0] = maxr[i-1][0]
            maxArea, maxR = updateMax(maxArea, maxR, (i,0), maxr[i][0])

        for j in range(1, colc, 1):

            if (matrix[i][j] == 0): 
                maxr[i][j] = None
                continue

            ii = maxr[i-1][j]
            jj = maxr[i][j-1]

            if (ii == None):
                if (jj == None):
                    maxr[i][j] = (i, j)
                else:
                    maxr[i][j] = (i, jj[1])
            else:
                 if (jj == None):
                    maxr[i][j] = (ii[0], j)
                 else:
                    maxr[i][j] = ii                    
                    #maxr[i][j] = (max(ii[0],jj[0]), max(ii[1], jj[1]))
            
            if (maxr[i][j][0] > i or maxr[i][j][1] > j):
                print(((i,j), maxr[i][j]))

            maxArea, maxR = updateMax(maxArea, maxR, (i,j), maxr[i][j])
    
    print(maxr)        
    return maxR 

m = [[1,0,1,0,0],
     [1,0,1,1,1],
     [1,1,1,1,1],
     [1,0,0,1,0]]

print("==========")
print(maxRect(m))

