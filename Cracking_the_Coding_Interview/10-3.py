
#calculate the determinant 
#  | p1[0] p1[1] 1 |
#  | p2[0] p2[1] 1 |
#  | p3[0] p3[1] 1 |

def crossDot(p1,p2,p3):
    main = p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1]
    sub = p3[1]*p1[0]+p1[1]*p2[0]+p2[1]*p3[0]
    return main-sub
    
def inLine(line, p1):
    if (line[1][0] == line[0][0]):
        xRatio = None
    else:     
        xRatio = (p1[0] - line[0][0])/(line[1][0] - line[0][0])    
        
    if (line[1][1] == line[0][1]):
        yRatio = None
    else:    
        yRatio = (p1[1] - line[0][1])/(line[1][1] - line[0][1])            
            
    return (xRatio == None or xRatio <= 1.0) and (yRatio == None or yRatio <= 1.0)         
    
def intersect(line1, line2):
    dot1 = crossDot(line1[0],line1[1],line2[0])
    dot2 = crossDot(line1[0],line1[1],line2[1])
    
    if (dot1 == 0.0 and inLine(line1, line2[0])):
        return True    

    if (dot2 == 0.0 and inLine(line1, line2[1])):
        return True    
        
    return (dot1 * dot2 < 0.0)    
    
line1 = [(0,1),(0,3)]
line2 = [(0,2),(2,2)]
line3 = [(1,2),(2,2)]
print("The intersection of {0} and {1} is {2}".format(line1, line2, intersect(line1, line2)))
print("The intersection of {0} and {1} is {2}".format(line1, line3, intersect(line1, line3)))
print("===============================")
line1 = [(1,0),(3,0)]
line2 = [(2,0),(2,2)]
line3 = [(2,1),(2,2)]
print("The intersection of {0} and {1} is {2}".format(line1, line2, intersect(line1, line2)))
print("The intersection of {0} and {1} is {2}".format(line1, line3, intersect(line1, line3)))

print("===============================")
line1 = [(1,0),(3,0)]
line2 = [(4,0),(5,0)]
line3 = [(2,0),(5,0)]
print("The intersection of {0} and {1} is {2}".format(line1, line2, intersect(line1, line2)))
print("The intersection of {0} and {1} is {2}".format(line1, line3, intersect(line1, line3)))