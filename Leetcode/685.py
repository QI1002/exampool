
#685. Redundant Connection II

def moreConn(links):

    mt = 0
    for a,b in links:
        if (a > mt): mt = a
        if (b > mt): mt = b
    
    depth = [ -1 for i in range(mt+1) ]
    result = []

    d = 0
    depth[links[0][0]] = 0
    for a,b in links:
        if (depth[a] == -1): 
            raise ValueError("wrong order")
        if (depth[b] == -1): 
            depth[b] = depth[a]+1
        else: 
            result.append([a,b])

    return result
       
links1 = [[1,2], [1,3], [2,3]]
print(moreConn(links1))

links2 = [[1,2], [2,3], [3,4], [4,1], [1,5], [5,4]]
print(moreConn(links2))
 
