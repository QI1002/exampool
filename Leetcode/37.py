
#37. Sudoku Solver
import copy
import timeit

class stack:
    def __init__(self):
        self.body = []

    def push(self, data):
        self.body.append(data)

    def pop(self):
        if (len(self.body) == 0):
            return None
        else:
            return self.body.pop()

    def isEmpty(self):
        return True if len(self.body) == 0 else False

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

def updateExists(exists, i, j, copy = False):
    new_exists = list(exists) if (copy) else exists
    new_exists[i] += 1
    new_exists[9+j] += 1
    new_exists[18+(i/3)*3+(j/3)] += 1
    return new_exists

def getSelection(i, j, board, exists):
    first = i
    second = 9 + j
    third = 18 + 3*(i/3) + j/3
    
    remain = [ i for i in range(1,10,1) ]
    here = getboarddata(board, first)
    for i in here: 
        if (i in remain): remain.remove(i)             
    here = getboarddata(board, second)
    for i in here: 
        if (i in remain): remain.remove(i)
    here = getboarddata(board, third)
    for i in here: 
        if (i in remain): remain.remove(i)
    
    return remain 

debug = 1
def findnext(index, board, exists):
    global debug 

    positions = []

    if (index < 9):
        for i in range(9):
            if (board[index][i] == 0):
                r = getSelection(index, i, board, exists) 
                positions.append((index, i, r))
    else: 
        if (index < 18):
            for i in range(9):
                if (board[i][index-9] == 0):
                    r = getSelection(i, index-9, board, exists) 
                    positions.append((i, index-9, r))
        else:
            k = index - 18 
            for i in range(3):
                for j in range(3):
                    y = (k/3)*3+i
                    x = (k%3)*3+j
                    if (board[y][x] == 0): 
                        r = getSelection(y, x, board, exists)
                        positions.append((y, x, r))

    if (len(positions) == 0):
        print("xxxx")
        if (debug): 
            printboard(board)
            debug = 0
        return (-1,-1, [])

    min = 0
    for i in range(len(positions)):   
        if (len(positions[i][2]) < len(positions[min][2])):
            min = i

    #print(("====",positions, min, index))   
    return positions[min] 


def sudoku(board, exists = None):

    sStack = stack()
   
    if (exists == None): 
        exists = checkexists(board)

    while(True):

        max = -1
        for i in range(len(exists)):
            if (exists[i] == 9): continue
            if (max == -1): 
                max = i
                continue  
            if (exists[max] < exists[i]):
                max = i
    
        #print((max, exists))
        if (max == -1): return board

        i, j, candidates = findnext(max, board, exists)

        if (len(candidates) == 0):
            if (sStack.isEmpty()): return None
            else: 
                exists = sStack.pop()  
                board = sStack.pop()

        for k in range(len(candidates)-1, -1, -1):
            if (k != 0):
                new_exists = updateExists(exists, i, j, True)
                new_board = copy.deepcopy(board)
                new_board[i][j] = candidates[k]
                sStack.push(new_board)
                sStack.push(new_exists)
            else:
                new_exists = updateExists(exists, i, j, False)
                new_board = board
                new_board[i][j] = candidates[k]
    
    return None

def printboard(board):
    if (board == None): return
    for i in range(9):
        print(board[i])

data0 = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]

data1 = [[1,0,0,0,2,0,6,0,0],
         [0,0,3,8,7,4,0,9,5],
         [0,0,0,1,0,0,0,3,0],
         [0,3,0,0,5,0,4,2,0],
         [8,0,4,2,0,3,7,0,1],
         [0,2,5,0,1,0,0,6,0],
         [0,1,0,0,0,9,0,0,0],
         [4,5,0,6,3,1,8,0,0],
         [0,0,8,0,4,0,0,0,6]]

data2 = [[0,5,0,4,9,0,0,0,0],
         [2,0,7,0,0,5,0,0,9],
         [6,0,9,7,8,0,3,0,4],
         [5,0,0,0,6,0,2,0,0],
         [0,9,6,0,0,0,5,7,0],
         [0,0,8,0,5,0,0,0,3],
         [1,0,5,0,7,9,4,0,6],
         [9,0,0,5,0,0,8,0,7],
         [0,0,0,0,1,6,0,2,0]]

data3 = [[8,0,0,7,0,4,1,0,0],
         [5,1,0,0,2,0,0,0,7],
         [0,0,4,5,1,0,0,6,0],
         [0,0,5,0,0,0,6,7,0],
         [0,0,0,6,3,8,0,0,0],
         [0,2,8,0,0,0,3,0,0],
         [0,9,0,0,8,5,2,0,0],
         [3,0,0,0,6,0,0,5,9],
         [0,0,6,9,0,1,0,0,3]]

data4 = [[0,0,9,7,6,2,0,1,0],
         [0,0,0,3,0,0,7,5,0],
         [0,3,0,8,0,0,0,9,6],
         [0,0,4,0,0,5,0,6,0],
         [1,5,0,0,0,0,0,4,7],
         [0,8,0,4,0,0,3,0,0],
         [3,7,0,0,0,6,0,8,0],
         [0,1,8,0,0,4,0,0,0],
         [0,9,0,2,8,3,6,0,0]]


templates = [data0, data1, data2, data3, data4]
probe = 0
if (probe):
    value = min(timeit.repeat(stmt="sudoku(data0)", setup="from __main__ import sudoku, data0", number = 1000, repeat = 5))
    print(value)
else:
    for x in templates:
        printboard(sudoku(x))
        print("============================")
