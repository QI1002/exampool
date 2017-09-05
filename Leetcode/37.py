
#37. Sudoku Solver
import copy

def getboarddata(board, index):
    if (index < 9):
        return [ board[index][i] for i in range(9) ] 
    if (index < 18):
        return [ board[i][index-9] for i in range(9) ]
   
    index -= 18 
    y, x = 3*(index/3), 3*(index%3)
    result = []
    result.extend(board[y+0][x:x+3])
    result.extend(board[y+1][x:x+3])
    result.extend(board[y+2][x:x+3])
    
    return result 

def checkexists(board):
    exists = [] 
    for i in range(9):
        e = 0
        for j in range(9):
            if (board[i][j] != 0): e += 1
        exists.append(e)

    for i in range(9):
        e = 0
        for j in range(9):
            if (board[j][i] != 0): e += 1
        exists.append(e)

    for i in range(3):
        for j in range(3):
            e = 0
            for k1 in range(3):
                for k2 in range(3):
                    if (board[3*i+k1][3*j+k2] != 0): e += 1 
            exists.append(e)      

    return exists

def updateExists(exists, i, j):
    exists[i] += 1
    exists[9+j] += 1
    exists[18+(i/3)*3+(j/3)] += 1
    return list(exists)

def getSelection(i, j, index, exists):
    first1 = i
    second1 = 9 + j
    third1 = 18 + 3*(i/3) + j/3
    first2 = 0 if (first1 == index) else exists[first1]        
    second2 = 0 if (second1 == index) else exists[second1]
    third2 = 0 if (third1 == index) else exists[third1]

    if (first2 > second2 and first2 > third2): return first1, first2
    if (second2 > first2 and second2 > third2): return second1, second2
    return third2, third1 

def findnext(index, board, exists):

    positions = []

    if (index < 9):
        for i in range(9):
            if (board[index][i] == 0):
                p, c = getSelection(index, i, index, exists) 
                positions.append((index, i, p, c))
    else: 
        if (index < 18):
            for i in range(9):
                if (board[i][index-9] == 0):
                    p, c = getSelection(i, index-9, index, exists) 
                    positions.append((i, index-9, p, c))
        else:
            k = index - 18 
            for i in range(3):
                for j in range(3):
                    y = (k/3)*3+i
                    x = (k%3)*3+j
                    if (board[y][x] == 0): 
                        p, c = getSelection(y, x, index, exists)
                        positions.append((y, x, p, c))

    if (len(positions) == 0):
        return (-1,-1), []

    max = 0
    for i in range(len(positions)):   
        if (positions[i][2] < positions[max][2]):
            max = i
   
    print((positions, max)) 
    remain = [ i for i in range(1,10,1) ]
    here = getboarddata(board, index)
    print(here)
    for i in here: 
        if (i in remain): remain.remove(i)             
    c = positions[max][3]
    print(c)
    there = getboarddata(board, c)
    print(there)
    for i in there: 
        if (i in remain): remain.remove(i)
    
    return (positions[max][0], positions[max][1]), remain 


def sudoku(board, exists = None):
   
    if (exists == None): 
        exists = checkexists(board)

    max = 0
    for i in range(len(exists)):
        if (exists[max] < exists[i]):
            max = i

    if (exists[max] == 9):
        return board

    (i,j), candidates = findnext(max, board, exists)
    print(max,(i,j), candidates)
    for k in range(len(candidates)):
        exists = updateExists(exists, i, j)
        new_board = copy.deepcopy(board) if (k != 0) else board
        board[i][j] = candidates[k]
        result = sudoku(board, exists)
        if (result != None): return result
    
    return None

def printboard(board):
    if (board == None): return
    for i in range(9):
        print(board[i])

data = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

printboard(sudoku(data))
