
#11. Container with Most Water

def myContainMost(data):
    count = len(data)
    m = [ (j,i) for i,j in enumerate(data) ]
    ms = sorted(m)
    l = ms.pop()
    r = ms.pop()
    max = l[1] if l[1]>r[1] else r[1]
    min = r[1] if l[1]>r[1] else l[1]
    maxarea = (max-min) * r[0]
    while(len(ms) != 0):
        n = ms.pop()
        if ((n[0]*count) < maxarea): break

        if ((n[1]-min) > (max-n[1])):
            mm = (n[1]-min)*n[0]
        else:
            mm = (max-n[1])*n[0]
            
        if (mm > maxarea): maxarea = mm

        if (n[1] > max): max = n[1]
        if (n[1] < min): min = n[1]

    return maxarea

def containMost(data):
    l, r = 0, len(data)-1
    maxarea = 0
    while(l < r):
        min = data[r] if data[l] > data[r] else data[l]
        mm = (r-l)*min
        if (mm > maxarea): maxarea = mm
        if (data[l] > data[r]): r -= 1
        else: l += 1

    return maxarea

sample = [1,8,6,2,5,4,8,3,7]
print("{0}'s max area = {1},{2}".format(sample, myContainMost(sample), containMost(sample)))
