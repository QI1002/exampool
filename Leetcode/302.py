
#302. Smallest Rectangel Enclosing Black Pixels 

def enclosingArea(data, seed):
    rowc = len(data)
    colc = len(data[0])

    if (seed[0] < 0 or seed[0] >= colc):
        raise ValueError("Wrong Seed")
    
    if (seed[1] < 0 or seed[1] >= rowc):
        raise ValueError("Wrong Seed")

    if (data[seed[1]][seed[0]] != '1'):
        raise ValueError("Wrong Seed")

    (l,t),(r,b) = seed, seed
    black = [ seed ] 
    i = 0
    while(i < len(black)):
        j = len(black)
        for k in range(i, j):
            x = black[k][0]
            y = black[k][1]
            if (x > 0 and data[y][x-1] == '1'):
                if ((x-1) < l): l = x-1
                if (not (x-1,y) in black):
                    black.append((x-1,y))
            if (y > 0 and data[y-1][x] == '1'):
                if ((y-1) < t): t = y-1
                if (not (x,y-1) in black):
                    black.append((x,y-1))
            if ((x+1) < colc and data[y][x+1]== '1'):
                if ((x+1) > r): r = x+1
                if (not (x+1,y) in black):
                    black.append((x+1,y))
            if ((y+1) < rowc and data[y+1][x] == '1'):
                if ((y+1) > b): b = y+1
                if (not (x,y+1) in black):
                    black.append((x,y+1))
        print(black)        
        i = j

    area = (r-l+1)*(b-t+1)
    return area, (l,t,r,b)


given = [ "0010", "0110", "0100" ]
seed = (2, 0)
print("{0}:{1}".format((given, seed), enclosingArea(given, seed)))
        




