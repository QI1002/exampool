
#305. Number of Islands II 

def neighbor(a, b):
    d = abs(a[0]-b[0]) + abs(a[1]-b[1])
    return (d == 1)

def numIslands(data):
    
    if (len(data) == 0): return 0

    island = [ [data[0]] ]
    result = [1]
    for i in range(1, len(data)):
        base = island
        island = []
        ii = data[i]
        j = None
        for ss in base:
            nn = False
            for s in ss: 
                if (neighbor(s, ii) == False): continue
                nn = True
                if (j == None):
                    island.append(ss)
                    j = len(island)-1
                else:    
                    island[j].extend(ss)
                island[j].append(ii)
                break
            if (nn == False): island.append(ss)
        if (j == None): island.append([ii])

        result.append(len(island))       
        print(island)
    
    return result

given = [ (0,0),(0,1),(2,2),(2,1) ]
print("{0}:{1}".format(given, numIslands(given)))
given = [ (0,0),(0,1),(2,2),(2,1),(1,1) ]
print("{0}:{1}".format(given, numIslands(given)))
        




