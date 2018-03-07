
#317. Shorted Distance from All Buildings 

import copy 
def shortest(data, seed):
    rowc = len(data)
    colc = len(data[0])
    max = rowc*colc
    r = [ rowc*colc for i in range(colc) ]
    result = [ list(r) for i in range(rowc) ]

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
   
    #print((seed, result))
    return result

def shortestAll(data):
    rowc = len(data)
    colc = len(data[0])
    max = rowc * colc

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
            skip = False
            for sss in ss: 
                if (sss[j][i] == max): 
                    skip = True
                    break
                sum += sss[j][i]
            if (skip): continue    
            if (min == None or min > sum):
                min, mini = sum, (j,i)

    return min, mini

given = [ "10201", "00000", "00100" ]
print("{0}:{1}".format((given), shortestAll(given)))
given = [ "10201", "10000", "00100" ]
print("{0}:{1}".format((given), shortestAll(given)))
given = [ "10201", "00010", "00100" ]
print("{0}:{1}".format((given), shortestAll(given)))
given = [ "10201", "00200", "00100" ]
print("{0}:{1}".format((given), shortestAll(given)))
        




