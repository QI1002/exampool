
#286. Walls and Gates

def minDist(room):
    rowc = len(room)
    colc = len(room[0])

    update = True
    while(update):
        update = False
        for j in range(rowc):
            for i in range(colc):
                if (room[j][i] == 255): continue
                if (room[j][i] == -1): continue
                n = room[j][i]+1
                if (j > 0 and room[j-1][i] > n): 
                    update, room[j-1][i] = True, n 
                if (i > 0 and room[j][i-1] > n): 
                    update, room[j][i-1] = True, n 
                if ((j+1) < rowc and room[j+1][i] > n): 
                    update, room[j+1][i] = True, n 
                if ((i+1) < colc and room[j][i+1] > n): 
                    update, room[j][i+1] = True, n

    return room                

room = [[255, -1, 0, 255],
        [255, 255, 255, -1], 
        [255, -1, 255, -1], 
        [0, -1, 255, 255]]

print(minDist(room))
