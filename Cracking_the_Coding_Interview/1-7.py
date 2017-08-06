
mark = 99
def genMatrix(n, offset=0, zeros=[]):
    id = offset
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(id)
            id += 1
        matrix.append(row)

    for i in range(len(zeros)):
        x = zeros[i][0]
        y = zeros[i][1]
        if (x >=0 and y >=0 and x < n and y < n):
            matrix[y][x] = mark

    return matrix

def printMatrix(matrix):
    count = len(matrix)
    for i in range(count):
        print(matrix[i])

def list_add(ll, value):
    if not value in ll:
        ll.append(value)

def zeroMatrix(matrix):
    colnum = len(matrix)
    rownum = len(matrix[0])
    cols = []
    rows = []
    for i in range(rownum):
        for j in range(colnum):
            if (matrix[i][j] == mark):
                list_add(cols, j)
                list_add(rows, i)
    #print(cols)
    #print(rows)
    for k in cols:
        for i in range(rownum):
            matrix[i][k] = mark

    for k in rows:
        for i in range(colnum):
            matrix[k][i] = mark


dim = 7
offset = 10
zeros = [ (2,3), (6,6) ]
sample = genMatrix(dim, offset, zeros)
printMatrix(sample)
print("=================")
sampleZero = list(sample)
zeroMatrix(sampleZero)
printMatrix(sampleZero)