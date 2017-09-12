
#57. Insert Interval

import copy
def search(points, p):
    l = 0
    r = len(points)-1
    while (r >= l):
        m = (r+l)//2
        #print((m,r,l))
        if (points[m] == p): return m 
        if (m == l):
            if (points[l] > p): return l
            else: return r if (points[r] > p) else r+1 
        else:
            if (points[m] < p):
                l = m
            else:
                r = m

def line_merge_2(lines, target):
    count = len(lines)
    points = []
    for i in range(count):    
        points.append(lines[i][0])
        points.append(lines[i][1])

    s = search(points, target[0])
    e = search(points, target[1])
    #print((s,e,points))

    if (s == e):
        if (e < len(points) and points[e] == target[1]):
            lines[e//2] = (target[0], lines[e//2][1])
        else:
            lines.insert(s//2, target)
        return lines

    ss = s//2 
    if ((s & 0x01) == 0):  lines[ss] = (target[0], lines[ss][1])
    ee = (e-1)//2
    if ((e & 0x01) == 0):  
        if (e < len(points) and points[e] == target[1]):
            ee = e//2
            lines[ee] = (target[0], lines[ee][1]) 
        else: 
            lines[ee] = (lines[ee][0], target[1])

    for i in range(ss+1, ee, 1):
        lines.pop(ss+1)
    
    if ( (ss+1) < len(lines) and lines[ss][1] == lines[ss+1][0]):
        lines[ss] = (lines[ss][0], lines[ss+1][1])
        lines.pop(ss+1)
    
    return lines

def line_merge(lines, target):
    count = len(lines)
    points = []
    for i in range(count):    
        points.append(lines[i][0])
        points.append(lines[i][1])

    s = search(points, target[0])
    e = search(points, target[1])
    result = []
    extra = newline = newline2 = None

    for i in range(count):
        line = lines[i]

        if (s == 2*i):    
            newline = (target[0], line[1])         
        else:
            if (s == (2*i+1)):
                newline = line
        
        if (e == 2*i):
            if (lines[i][0] != target[1]):
                newline2 = (newline[0], target[1])
                extra = lines[i]
            else:
                newline2 = (newline[0], lines[i][1])
        else:
            if (e == (2*i+1)): 
                newline2 = (newline[0], lines[i][1])          

        if (s//2 > i or e//2 < i):
            result.append(line)

        if (newline2 != None):
            result.append(newline2)
            newline = newline2 = None

        if (extra != None):
            result.append(extra)
            extra = None
    
    if (newline != None and newline2 == None):
        newline2 = (newline[0], target[1]) 
        result.append(newline2)
     
    if (s >= len(points)):
        result = list(lines)
        result.append(target)

    return result
 
lines = [(2,3),(5,8),(11,13)]
print(line_merge(copy.deepcopy(lines), (9,10)))
print(line_merge(copy.deepcopy(lines), (9,11)))
print(line_merge(copy.deepcopy(lines), (8,10)))
print(line_merge(copy.deepcopy(lines), (8,11)))
print(line_merge(copy.deepcopy(lines), (14,16)))
print(line_merge(copy.deepcopy(lines), (0,1)))
print(line_merge(copy.deepcopy(lines), (4,14)))
print(line_merge(copy.deepcopy(lines), (0,10)))
print(line_merge(copy.deepcopy(lines), (0,14)))

 
