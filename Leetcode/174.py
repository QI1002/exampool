
#174. Dungeon Game

def dungeon(rooms):
    m = len(rooms)
    n = len(rooms[0])
    row = [ 0 for i in range(n) ]
    r = [ list(row) for i in range(m) ]
    h = [ list(row) for i in range(m) ]
    p = [ list(row) for i in range(m) ]

    r[0][0] = h[0][0] = rooms[0][0]
    for j in range(1,n,1):
        r[0][j] = r[0][j-1]+rooms[0][j]
        h[0][j] = r[0][j] if (r[0][j] < h[0][j-1]) else h[0][j-1]
        p[0][j] = 'h'
    for i in range(1,m,1):
        r[i][0] = r[i-1][0]+rooms[i][0]
        h[i][0] = r[i][0] if (r[i][0] < h[i-1][0]) else h[i-1][0]
        p[i][0] = 'v'

    for i in range(1,m,1):
        for j in range(1,n,1):
            hh = r[i][j-1] + rooms[i][j]
            vv = r[i-1][j] + rooms[i][j]
            #r[i][j] = hh if (hh > vv) else vv
            hhh = hh if (hh < h[i][j-1]) else h[i][j-1]
            vvv = vv if (vv < h[i-1][j]) else h[i-1][j]
            r[i][j] = hh if (hhh > vvv) else vv
            h[i][j] = hhh if (hhh > vvv) else vvv            
            p[i][j] = 'h' if (hhh > vvv) else 'v'                

    #print(r)
    #print(h)
    #print(p)

    i = m-1
    j = n-1
    health = 0
    path = []
    while(i != 0 or j != 0):
        if (health > h[i][j]): health = h[i][j]
        path.insert(0, (i, j))
        if (p[i][j] == 'v'):
            i -= 1
        else:
            j -= 1

    if (health > h[i][j]): health = h[i][j]
    path.insert(0, (0,0))

    return -health+1, path

games = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(dungeon(games))

games = [[-2,-3,3],[-5,0,1],[10,30,-5]]
print(dungeon(games))