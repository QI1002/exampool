
#363. Max Sum of Rectangle No Larger Than K

def maxSumSubRect2(matrix, k):
    rowc = len(matrix)
    colc = len(matrix[0])
    maxi = maxk = None

    for y1 in range(rowc):
        for x1 in range(colc):
            for y2 in range(y1+1):
                for x2 in range(x1+1):
                    sum = 0
                    for h in range(y2, y1+1, 1):
                        for w in range (x2, x1+1, 1):
                            sum += matrix[h][w]
                    if (sum <= k):
                        if (maxk == None or sum > maxk):
                            maxk = sum
                            maxi = ((y1,x1),(y2,x2))
    return maxk, maxi

def maxSumSubRect(matrix, k):
    rowc = len(matrix)
    colc = len(matrix[0])
    maxi = maxk = None

    sr = [ 0 for i in range(colc) ]
    s = [ list(sr) for i in range(rowc) ]

    for i in range(rowc):
        for j in range(colc):
            s[i][j] += matrix[i][j]
            if (i != 0): s[i][j] += s[i-1][j]
            if (j != 0): s[i][j] += s[i][j-1]
            if (i != 0 and j != 0): s[i][j] -= s[i-1][j-1]

    #print(s)

    for y1 in range(rowc):
        for x1 in range(colc):
            for y2 in range(y1+1):
                for x2 in range(x1+1):
                    sum = s[y1][x1]
                    if (x1 != x2 and x2 != 0): sum -= s[y1][x2-1]
                    if (y1 != y2 and y2 != 0): sum -= s[y2-1][x1]
                    if (x1 != x2 and y1 != y2 and x2 != 0 and y2 != 0): sum += s[y2-1][x2-1]
                    #print(sum,(y1,x1),(y2,x2))
                    if (sum <= k):
                        if (maxk == None or sum > maxk):
                            maxk = sum
                            maxi = ((y1,x1),(y2,x2))
    return maxk, maxi

samples = [[1,0,1],[0,-2,3]]
print(maxSumSubRect(samples, 2))
print(maxSumSubRect2(samples, 2))

samples = [[1,2,3],
           [4,5,6],
           [7,8,9]]
print(maxSumSubRect(samples, 22))
print(maxSumSubRect2(samples, 22))

samples = [[ 1, 2, 3, 4],
           [ 5, 6, 7, 8],
           [ 9,10,11,12],
           [13,14,15,16]]
print(maxSumSubRect(samples, 22))
print(maxSumSubRect2(samples, 22))
