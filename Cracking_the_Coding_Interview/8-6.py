

def paintBox(point, box):

    x = point[0]
    y = point[1]
    
    if (x < 0 or x >= len(box[0])):
        return
      
    if (y < 0 or y >= len(box)):
        return
                    
    if (box[y][x] == 1):
        return
        
    box[y][x] = 1        
    paintBox((x-1,y), box)    
    paintBox((x+1,y), box)
    paintBox((x,y-1), box)
    paintBox((x,y+1), box)
    
box = []    
m = 4
n = 6
for i in range(n):
    box.append([])
    for j in range(m):
        box[i].append(0)
        
point = (2,3)
paintBox(point, box)
print(box)