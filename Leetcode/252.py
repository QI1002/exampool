
#252. Meeting Rooms

def overlay(a, b):
    if (a[0] <= b[0] and b[0] < a[1]):
        return True
    if (b[0] <= a[0] and a[0] < b[0]):
        return True

    return False

def meetingAll(m):
    for i in range(len(m)):
        for j in range(i+1,len(m)):
            if (overlay(m[i],m[j])):
                return False

    return True

def meetingAll2(m):
    ms = sorted(m)
    a = m[0]
    for i in range(1, len(m)):
        if (overlay(a, m[i])): return False
        a = m[1]
    return True

data = [[0,30],[5,10],[15,20]]
print("{0}:{1}".format(data, meetingAll(data)))
print("{0}:{1}".format(data, meetingAll2(data)))
