
#317. Shorted Distance from All Buildings 

import copy 
def shortest(data, seed):
    rowc = len(data)
    colc = len(data[0])
    r = [ 0 for i in range(colc) ]
    result = [ list(r) for i in range(rowc) ]

    for j in range(rowc):
        for i in range(colc):
            if (data[j][i] != '0'): result[j][i] = -2
            result[j][i] = rowc*colc
    
    result[seed[0]][seed[1]] = 0
    update = True
    while(update):
        update = False
        for y in range(rowc):
            for x in range(colc):
                if data[y][x] != '0': continue
                m = result[y][x]
                if (x > 0 and (result[y][x-1]+1) < m):
                    update, result[y][x] = True, result[y][x-1]+1
                if (y > 0 and (result[y-1][x]+1) < m):
                    update, result[y][x] = True, result[y-1][x]+1
                if ((x+1) < colc and (result[y][x+1]+1) < m):
                    update, result[y][x] = True, result[y][x+1]+1
                if ((y+1) < rowc and (result[y+1][x]+1) < m):
                    update, result[y][x] = True, result[y+1][x]+1
   
    print((seed, result))
    return result

def shortestAll(data):
    rowc = len(data)
    colc = len(data[0])

    buildings = [ ]
    for j in range(rowc):
        for i in range(colc):
            if data[j][i] == '1': 
                buildings.append((j,i))

    ss = []
    for seed in buildings: 
        sss = shortest(data, seed)
        ss.append(sss)
    
    min = mini = None
    for j in range(rowc):
        for i in range(colc):
            if data[j][i] != '0': continue
            sum = 0
            for sss in ss: sum += sss[j][i]
            if (min == None or min > sum):
                min, mini = sum, (j,i)

    return min, mini

given = [ "10201", "00000", "00100" ]
print("{0}:{1}".format((given), shortestAll(given)))
        




