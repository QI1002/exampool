
#149. Max points on a line

def generatePoints(a, b, aofst = 1, bofst = 1):
    points = []
    for i in range(a):
        for j in range(b):
            points.append((aofst*i,bofst*j))
    return points
    
def minMultiple(a, b):

    if (a == 0 or b == 0): return 0
    while (a != b):
        if (a > b): a -= b
        else: b -= a
    
    return a 
    
def maxPointsOnLine(points):
    count = len(points)
    pairs = []
    lines = {}
    for i in range(count):
        for j in range(i+1, count, 1):
            pairs.append((points[i],points[j]))
            
    for k in range(len(pairs)):
        pair = pairs[k]
        dx = pair[0][0] - pair[1][0]
        dy = pair[0][1] - pair[1][1]
        
        mm = minMultiple(abs(dx), abs(dy))
        if (mm != 0): dx, dy = dx // mm, dy // mm
        if (dy < 0): dx, dy = -dx, -dy
        c = dy * pair[0][0] - dx * pair[0][1]
        key = (dx,dy,c)
        if not key in lines:
            lines[key] = [ pair[0], pair[1] ]
        else:
            if (not pair[0] in lines[key]):
                lines[key].append(pair[0])
            if (not pair[1] in lines[key]):
                lines[key].append(pair[1])
    
    maxline = []
    for key in lines:
        if (len(maxline) < len(lines[key])):
            maxline = lines[key]
            
    return maxline
                   
p = generatePoints(3, 2)                                          
print(maxPointsOnLine(p))    

p = generatePoints(2, 3)                                          
print(maxPointsOnLine(p)) 

p = generatePoints(2, 3, 2, 1)                                          
print(maxPointsOnLine(p)) 

p = generatePoints(2, 3, 1, 2)                                          
print(maxPointsOnLine(p)) 