
#329. Longest Increasing Path in a Matrix

import copy
def longPath(data):
    rowc = len(data)
    colc = len(data[0]) 
    
    path = []
    for i in range(rowc):
        for j in range(colc):
            if (i != 0 and data[i][j] < data[i-1][j]):
                path.append([(i,j),(i-1,j)])
            if (j != 0 and data[i][j] < data[i][j-1]):
                path.append([(i,j),(i,j-1)])
            if ((i+1) != rowc and data[i][j] < data[i+1][j]):
                path.append([(i,j),(i+1,j)])
            if ((j+1) != colc and data[i][j] < data[i][j+1]):
                path.append([(i,j),(i,j+1)])
    
    #print(path)      
    result = copy.deepcopy(path)
    updated = True            
    while(updated):
        updated = False
        base = result
        result = []
        for i in range(len(base)):
            for j in range(len(path)):    
                if (base[i][-1] == path[j][0]):
                    ll = list(base[i])
                    ll.append(path[j][1]) 
                    result.append(ll)
                    updated = True
    
    result = base
    #print(result)
    if (len(result) == 0):
        return None, None
                      
    max = 0
    maxi = 0
    for i in range(len(result)):                
        if (max < len(result[i])):                            
            max = len(result[i])
            maxi = i
    
    value = []
    r = result[maxi]
    for i in range(len(r)):
        value.append(data[r[i][0]][r[i][1]])
        
    return r, value
    
sample = [[9,9,4],
          [6,6,8],
          [2,1,1]]
          
print(longPath(sample))                      

sample = [[3,4,5],
          [3,2,6],
          [2,2,1]]
          
print(longPath(sample))                      
