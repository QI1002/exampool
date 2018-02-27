
#253. Meeting Rooms II

def overlay(a, b):
    if (a[0] <= b[0] and b[0] < a[1]):
        return True
    if (b[0] <= a[0] and a[0] < b[0]):
        return True

    return False

def meetingMax(m):
    conflict = [ [] for x in m ]
    for i in range(len(m)):
        for j in range(i+1,len(m)):
            if (overlay(m[i],m[j])):
                conflict[i].append(j)
                conflict[j].append(i)

    while(len(conflict) > 0):        
        max = 0
        for i in range(1,len(conflict)):
            if (len(conflict[i]) > len(conflict[max])):
                max = i
        if (len(conflict[max]) == 0): break        
        for j in conflict[max]: conflict[j].remove(max)
        conflict.pop(max)

    return len(conflict)

data = [[0,30],[5,10],[15,20]]
print("{0}:{1}".format(data, meetingMax(data)))
