
def swap(l,i,j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

def min(a,b):
    if (a > b):
       return b
    else:
       return a   
       
def getSlope(x1,y1,x2,y2):
    if (x1 == x2):
        return 'NaN'
    return (y1-y2)/(x1-x2)
    
def generatePoints(a,b):
    points = []
    for i in range(a):
        for j in range(b):
            points.append((i,j))
    return points
                
def lineBySlope(points):
    slopes = {}
    count = len(points)
    for i in range(count):
        for j in range(i+1, count, 1):
             slope = getSlope(points[i][0], points[i][1], points[j][0], points[j][1])
             if not slope in slopes:
                 slopes[slope] = []
             slopes[slope].append(((points[i][0], points[i][1]),(points[j][0], points[j][1])))
    return slopes
    
def maxPointsInline(points, lines):
    max_points = []
    points_group = []
    point_count = len(points)
    line_count = len(lines)
    for i in range(point_count):
        points_group.append(i)
        
    for j in range(line_count):    
        s_index = points.index(lines[j][0])
        e_index = points.index(lines[j][1])        
        group_min = min(points_group[s_index], points_group[e_index])
        group_max = group_min ^ points_group[s_index] ^ points_group[e_index]            
        
        for i in range(point_count):
            if (points_group[i] == group_max):
                points_group[i] = group_min
            
    point_max = {}
    for i in range(point_count):
        v = points_group[i]
        if not (v in point_max):
            point_max[v] = 1
        else:
            point_max[v] += 1
            
    max = 0
    for i in point_max:
        if (point_max[i] > point_max[max]):
            max = i
                
    for i in range(point_count):
        if (points_group[i] == max):
            max_points.append(points[i])
                
    return max_points

def slope_sort(slopes):
    result = {} 
    lengths = []
    keys = list(slopes.keys())
    count = len(slopes)
    
    for i in range(count):
        key = keys[i]
        lengths.append(len(slopes[key]))        

    for i in range(count):    
        max = i
        for j in range(i+1, count, 1):
            if (lengths[j] > lengths[max]):
                max = j
        swap(lengths, max, i)        
        swap(keys, max, i)
        
    return keys
        
def findMaxPoints():
    points = generatePoints(2,3)
    slopes = lineBySlope(points)
    keys = slope_sort(slopes)
    max_points = []

    for key in keys:
        #print(str(key) + ":" + str(slopes[key]))
        max_points_ = maxPointsInline(points, slopes[key])
        #print(max_points_);
        #print("==============");
        if (len(max_points_) > len(max_points)):
            max_points = max_points_        
        
    return max_points
                 
print(findMaxPoints())