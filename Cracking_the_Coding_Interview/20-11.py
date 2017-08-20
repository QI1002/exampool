
import random

def genBinaryMatrix(m,n):
    matrix = []
    for y in range(n):
        matrix.append([])
        for x in range(m):
            v = random.randint(0,3)
            matrix[y].append(1 if (v > 0) else 0)
    return matrix   
    
def printMatrix(matrix):
    count = len(matrix)
    for i in range(count):
        print(matrix[i])
    
def search_square(n):
    result = []
    for size in range(n, 0, -1):
        for i in range(0, n-size+1, 1):
            for j in range(0, n-size+1, 1):
                result.append((i, j, size))
    
    return result
                
def checkSquare1(data):
    squares = search_square(len(data))
    #print(squares)
    for square in squares: 
        found = True
        y = square[0]
        x = square[1]
        size = square[2]
        for i in range(x, x+size, 1):
            if (data[y][i] != 1 or data[y+size-1][i] != 1): 
              found = False
              break

        if (found == False):
            continue
                    
        for i in range(y+1, y+size-1, 1):
            if (data[i][x] != 1 or data[i][x+size-1] != 1):
              found = False
              break
              
        if (found):
            return square
            
    return None
                
#mat = [[1, 1, 1, 0, 1],[1, 1, 0, 1, 1],[0, 1, 1, 1, 1],[1, 1, 1, 1, 0],[1, 1, 1, 1, 1]]          
mat = genBinaryMatrix(5,5)                                 
printMatrix(mat)
print(checkSquare1(mat))