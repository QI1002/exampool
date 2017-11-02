
#335. Self Crossing 

def cross(line1, line2):
    v1 = (line1[0][0] == line1[1][0])
    v2 = (line2[0][0] == line2[1][0])
   
    if (v1): 
        s1, s2, s3 = line1[0][0],line1[0][1],line1[1][1]
    else:
        s1, s2, s3 = line1[0][1],line1[0][0],line1[1][0]

    if (v2): 
        e1, e2, e3 = line2[0][0],line2[0][1],line2[1][1]
    else:
        e1, e2, e3 = line2[0][1],line2[0][0],line2[1][0]

    #print((v1,s1,s2,s3),(v2,e1,e2,e3))
    if (v1 == v2):
        if (s1 == e1):
            return ((s2 <= e2 and e2 <= s3) or (e2 <= s2 and s2 <= e3))
        else:   
            return False 
    else:
        return ((s2 <= e1 and e1 <= s3) and (e2 <= s1 and s1 <= e3))

def selfCross(data):
    lines = []
    origin = (0,0)
    for i in range(len(data)):
        if ((i & 0x1) == 0):
            if ((i & 0x2) == 0):
                end = (origin[0], origin[1]+data[i])
            else:
                end = (origin[0], origin[1]-data[i])
        else:    
            if ((i & 0x2) == 0):
                end = (origin[0]-data[i], origin[1])
            else:
                end = (origin[0]+data[i], origin[1])
 
        lines.append((origin, end))
        origin = end

    #print(lines)

    for i in range(len(lines)):
        for j in range(len(lines)):
            if (abs(i-j) <= 1):  continue
            if (cross(lines[i], lines[j])):
                #print((lines[i], lines[j]))
                return True

    return False
           
segs = [2,1,1,2]
print("{0} = {1}".format(segs, selfCross(segs)))   

segs = [1,2,3,4]
print("{0} = {1}".format(segs, selfCross(segs)))   

segs = [1,1,1,1]
print("{0} = {1}".format(segs, selfCross(segs)))   
 
