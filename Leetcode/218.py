

#218. The Skyline Problem 

def swap(data, a, b):
    tmp = data[a]
    data[a] = data[b]
    data[b] = tmp
    
def hsort(buildings):
   count = len(buildings)
   for i in range(count):
       max = i
       for j in range(i+1, count, 1):
           if (buildings[max][2] < buildings[j][2]):
               max = j
       swap(buildings, i, max)

def intersect(line1, line2):
    #print((line1, line2))
    if (line1[0] < line2[0] and line2[0] < line1[1]):
        if (line2[1] > line1[1]): return (line2[0], line1[1])
        else: return line2
    if (line2[0] < line1[0] and line1[0] < line2[1]):
        if (line1[1] > line2[1]): return (line1[0], line2[1])
        else: return line1
    
    return None
    
def skyline(buildings):
    if (len(buildings) == 0): return []
    result = [ buildings[0] ]
    for i in range(1,len(buildings),1):
        b = buildings[i]
        base = list(result)
        #print(base)
        result = []
        
        if (b[0] < base[0][0]):
            if (b[1] < base[0][0]): result.append(b)
            else: result.append((b[0], base[0][0], b[2]))
            
        for j in range(len(base)-1):
            result.append(base[j])
            start = base[j][1]
            end = base[j+1][0]
            if (start == end): continue
            i = intersect((start,end), (b[0],b[1]))
            if (i != None): result.append((i[0],i[1],b[2]))
            
        result.append(base[len(base)-1])
        if (b[1] > base[len(base)-1][1]):
            if (b[0] > base[len(base)-1][1]): result.append(b)
            else: result.append((base[len(base)-1][1], b[1], b[2]))
                        
    return result
            
buildings = [(2,9,10), (3,7,15), (5,12,12), (15,20,10), (19,24,8)]   
hsort(buildings)
print(buildings)
print(skyline(buildings))
print("==========================")
buildings = [(1,30,10), (3,7,15), (5,12,12), (2,9,10), (19,24,8)]   
hsort(buildings)
print(buildings)
print(skyline(buildings))