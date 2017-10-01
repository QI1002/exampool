
#174. Dungeon Game

def dungeon(rooms):
    m = len(rooms)
    n = len(rooms[0])
    row = [ 0 for i in range(n) ]
    h = [ list(row) for i in range(m) ]
    p = [ list(row) for i in range(m) ]
    
    h[0][0] = rooms[0][0]
    for j in range(1,n,1):
        t = h[0][j-1]+rooms[0][j]
        h[0][j] = t if (t < h[0][j-1]) else h[0][j-1]
        p[0][j] = 'h'
    for i in range(1,m,1):
        t = h[i-1][0]+rooms[i][0]
        h[i][0] = t if (t < h[i-1][0]) else h[i-1][0]
        p[i][0] = 'v'
        
    for i in range(1,m,1):
        for j in range(1,n,1):
            hh = h[i][j-1]
            vv = h[i-1][j]
            h[i][j] = hh if (hh > vv) else vv              
            p[i][j] = 'h' if (hh > vv) else 'v'              
            if (rooms[i][j] < 0):
                h[i][j] += rooms[i][j]
                
    print(h)    
    print(p)
    
    i = m-1
    j = n-1
    health = 0
    path = []
    while(i != 0 or j != 0):
        health += rooms[i][j]
        path.insert(0, (i, j))
        if (p[i][j] == 'v'):
            i -= 1
        else:
            j -= 1
        
    health += rooms[0][0]                
    path.insert(0, (0,0))
        
    return -health+1, path
    
#games = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
games = [[-2,-3,3],[-5,0,1],[10,30,-5]]
print(dungeon(games))         
    