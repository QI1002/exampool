
#85. Maximal Rectangle

def updateMax(maxArea, maxR, posE, posS):
    area = (posE[0]-posS[0]+1)*(posE[1]-posS[1]+1)
    #print((posS, posE, area, maxArea))
    if (area > maxArea):
        maxArea = area
        maxR = posE,posS

    return maxArea, maxR

def overlay(a, b):
    if (a[0] <= b[0] and b[0] <= a[1]):
        if (b[1] > a[1]): return (b[0], a[1])
        else: return b 
   
    if (b[0] <= a[0] and a[0] <= b[1]):
        if (a[1] > b[1]): return (a[0], b[1])
        else: return a
 
    return None 

def maxRect(matrix):
    rowc = len(matrix)
    colc = len(matrix[0])
    maxArea = 0
    maxR = None
    segs = [[] for i in range(rowc)]
    for i in range(rowc):
        start = -1
        for j in range(colc+1):
            if (j < colc and matrix[i][j] == 1):
                if (start == -1): start = j
            else:
                if (start != -1): 
                    segs[i].append((start, j-1))
                    maxArea, maxR = updateMax(maxArea, maxR, (i, j-1), (i, start))
                    start = -1

        #print(segs[i]) 

        for j in range(i-1, -1, -1):
            ii = jj = 0
            imm = []
            while (ii < len(segs[i]) and jj < len(segs[j])): 
                ov = overlay(segs[i][ii], segs[j][jj])
                if (ov != None): 
                    imm.append(ov)
                    maxArea, maxR = updateMax(maxArea, maxR, (i, ov[1]), (j, ov[0]))

                if (segs[i][ii][1] > segs[j][jj][1]): jj += 1
                else: ii += 1
                        
            segs[j] = imm

    return maxR, maxArea 

m1 = [[1,0,1,0,0],
      [1,0,1,1,1],
      [1,1,1,1,1],
      [1,0,0,1,0]]

m2 = [[1,0,1,0,0],
      [1,0,1,0,1],
      [1,1,1,1,1],
      [1,0,0,1,0]]

m3 = [[0,1,1,0,0],
      [0,1,1,0,1],
      [1,1,1,1,1],
      [1,0,0,1,0]]

print("==========")
print(maxRect(m1))
print("==========")
print(maxRect(m2))
print("==========")
print(maxRect(m3))

