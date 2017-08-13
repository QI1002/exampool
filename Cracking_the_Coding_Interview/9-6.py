
def printMatrix(matrix):
    count = len(matrix)
    for i in range(count):
        print(matrix[i])

def genRowFirstMatrix(m,n,offset):
    matrix = []
    for y in range(n):
        matrix.append([])
        for x in range(m):
            matrix[y].append(offset)
            offset += 1
    return matrix

def genColumnFirstMatrix(m,n,offset):
    matrix = []
    for y in range(n):
        matrix.append([])
        for x in range(m):
            matrix[y].append("")
            
    for x in range(m):
        for y in range(n):
            matrix[y][x] = offset
            offset += 1
    return matrix
            
def genZigZagMatrix(m,n,offset,rowfirst = True):

    matrix = []
    for y in range(n):
        matrix.append([])
        for x in range(m):
            matrix[y].append("")

    count = m + n - 1
    for i in range(count):
        for j in range(0,i+1,1):
            if (rowfirst):
                x = j
                y = i - x            
            else:
                y = j
                x = i - y
            
            if (x < m and y < n):
                matrix[y][x] = offset
                offset += 1
                #print(x, y)
        rowfirst = not rowfirst        
    return matrix

#   ll = 1  3 
#      minUpper maxLower
#   0     0       -1
#   2     1       0         
#   4     2       1
   
def findMinUpper(ll, v, l=0, r=None):
    if (r == None):
        r = len(ll)-1

    while(True):
        m = (l + r)//2
        #print(str(l)+ " " + str(r) + " " + str(m))
        vv = ll[m]
        if (vv == v):
            return m
        if (l == m):
            rr = ll[r]
            if (v == rr):
                return r
            else:                                        
                return (r+1 if (rr < v) else r) if (vv < v) else l
        else:
            if (vv < v):            
                l = m
            else:
                r = m
    
def findMaxLower(ll, v, l=0, r=None):
    if (r == None):
        r = len(ll)-1

    while(True):
        m = (l + r)//2
        #print(str(l)+ " " + str(r) + " " + str(m))
        vv = ll[m]
        if (vv == v):
            return m
        if (l == m):
            rr = ll[r]
            if (v == rr):
                return r
            else:                                        
                return (r if (rr < v) else r-1) if (vv < v) else l-1
        else:
            if (vv < v):            
                l = m
            else:
                r = m
                        
def findInMatrix(matrix, v):
    r = len(matrix[0])-1
    l = 0
    b = len(matrix)-1
    t = 0
    
    while(t < b and r < l):
        r = findMinUpper(matrix[t], v, l, r)
        if (r >= len(matrix[t])): r = len(matrix[t])-1        
        l = findMaxLower(matrix[b], v, l, r)
        if (l < 0): l = 0;
        print("{0},{1},{2},{3}".format(l, r, t, b))
        if (matrix[t][r] == v): return (t,v)
        if (matrix[b][l] == v): return (b,l)
        t = t+1
        b = b-1    
         
    return None
         
mat = genZigZagMatrix(6,4,11, True)
#mat = genZigZagMatrix(6,4,11, False)
#mat = genRowFirstMatrix(6,4,11)
#mat = genColumnFirstMatrix(6,4,11)
printMatrix(mat)

#basic test 
#basic = [ 1, 3 ]
#for i in range(5):
#    print("minUpper and maxLower of {0} is ({1},{2})".format(i, findMinUpper(basic,i), findMaxLower(basic,i)))
 
print(findInMatrix(mat, 18))
  