
#296. Best Meeting Point 

def meeting1D(d1):
    homes = sorted(d1)
    index = len(homes)//2
    return homes[index]

def meeting2D(d2):
    dx = [ x for x,y in d2 ]
    dy = [ y for x,y in d2 ]
    return (meeting1D(dx), meeting1D(dy))

def shortDist(d2):
    s = meeting2D(d2)
    d = 0
    for home in d2:
        d += abs(home[0]-s[0])
        d += abs(home[1]-s[1])
    return (s,d)

given = [(0,0),(0,4),(2,2)]
print("{0}:{1}".format(given, shortDist(given)))
