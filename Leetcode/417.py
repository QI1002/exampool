
#417. Trapping Rain Water II

def trapRain(blocks):
    colc = len(blocks[0])
    rowc = len(blocks)

    row = [ 0 for i in range(colc) ]
    m = [ list(row) for i in range(rowc) ]
    update = True
    max = 0

    for i in range(rowc):
        for j in range(colc):
            if (blocks[i][j] > max): max = blocks[i][j]

    max += 1

    while(update):
        update = False
        for i in range(1, rowc-1, 1):
            for j in range(1, colc-1, 1):
                if (m[i][j] != 0): continue
                min = max
                if (blocks[i-1][j] < min and m[i-1][j] == 0):
                    min = blocks[i-1][j]
                if (blocks[i+1][j] < min and m[i+1][j] == 0):
                    min = blocks[i+1][j]
                if (blocks[i][j-1] < min and m[i][j-1] == 0):
                    min = blocks[i][j-1]
                if (blocks[i][j+1] < min and m[i][j+1] == 0):
                    min = blocks[i][j+1]
                if (min > blocks[i][j]):
                    m[i][j] = min 
                    update = True
    return m                     

blocks = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

print(trapRain(blocks))
