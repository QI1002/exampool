def genMatrix(n, offset=0):
    id = offset
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(id)
            id += 1
        matrix.append(row)
    return matrix

def printMatrix(matrix):
    count = len(matrix)
    for i in range(count):
        print(matrix[i])

def swapCCW(square,x,d,count):
    tmp = square[d][d+x]
    square[d][d+x] = square[d+x][count-1-d]
    square[d+x][count-1-d] = square[count-1-d][count-1-x-d]
    square[count-1-d][count-1-x-d] = square[count-1-x-d][d]
    square[count-1-x-d][d] = tmp

def rotateCCW(matrix):
    count = len(matrix)
    half = count // 2
    for i in range(half):
        for j in range(count-i*2-1):
            swapCCW(matrix, j, i, count)
            #if (i == 0):
            #    printMatrix(matrix)
            #    print("____________________")

def swapCW(square,x,d,count):
    tmp = square[count-1-x-d][d]
    square[count-1-x-d][d] = square[count-1-d][count-1-x-d]
    square[count-1-d][count-1-x-d] = square[d+x][count-1-d]
    square[d+x][count-1-d] = square[d][d+x]
    square[d][d+x] = tmp

def rotateCW(matrix):
    count = len(matrix)
    half = count // 2
    for i in range(half):
        for j in range(count-i*2-1):
            swapCW(matrix, j, i, count)
            #if (i == 0):
            #    printMatrix(matrix)
            #    print("____________________")

dim = 7
offset = 10
sample = genMatrix(dim, offset)
printMatrix(sample)
print("=================")
sampleCCW = list(sample)
rotateCCW(sampleCCW)
printMatrix(sampleCCW)
print("=================")
sample = genMatrix(dim, offset)
sampleCW = list(sample)
rotateCW(sampleCW)
printMatrix(sampleCW)