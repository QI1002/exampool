
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

def line_merge2(lines, target):
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

def line_overlay2(lines, p, pp, ii):
    if (pp//2 != ii): return False
    even = ((pp & 0x1) == 0)
    if (even and lines[pp//2][0] == p): return True
    return (even == False)

def line_overlay(lines, p, pp, ii):
    return (lines[ii][0] <= p and lines[ii][1] >= p) 

def line_merge(lines, target):
    count = len(lines)
    points = []
    for i in range(count):
        points.append(lines[i][0])
        points.append(lines[i][1])

    s = search(points, target[0])
    e = search(points, target[1])
    result = []
    newline = None

    for i in range(count):
        overlay = False
        line = lines[i]
        if (line_overlay(lines, target[0], s, i)):
            overlay = True
            newline = line
        else:
           if (target[0] < line[0] and s == 2*i):
               newline = (target[0], line[1])
        #print((newline, line, e))
        if (line_overlay(lines, target[1], e, i)):
            newline = (newline[0], line[1])
            result.append(newline)
            overlay = True
            newline = None
        else:
            if (target[1] < lines[0] and e == 2*i):
                newline = (newline[0], target[1])
                result.append(newline)
                newline = None
        #print((newline, overlay, result, line, s))
        if (newline == None and overlay == False):
            result.append(line)

    if (newline != None):
        result.append((newline[0], target[1]))

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

 
