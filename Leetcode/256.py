
#256. Paint House 

def min(a, b):
    return a if a < b else b

def paint(cost):
    red = green = blue = 0
    n = len(cost)
    k = len(cost[0])
    if (k != 3): raise ValueError("value is not consistent")

    rt = []
    gt = []
    bt = []
    for i in range(n):
        r = cost[i][0] + min(green, blue)
        rtt = gt if (green < blue) else bt
        g = cost[i][1] + min(red, blue)
        gtt = rt if (red < blue) else bt
        b = cost[i][2] + min(red, green)
        btt = rt if (red < green) else gt

        red = r
        green = g
        blue = b
        print((r,g,b,rtt,gtt,btt))
        rt = list(rtt)
        rt.append(0)
        gt = list(gtt)
        gt.append(1)
        bt = list(btt)
        bt.append(2)
    if (red <= green and red <= blue):
        return red, rt
    if (green <= red and green <= blue):
        return green, gt
    
    return blue, bt


cost = [[1,3,2],[4,1,2],[2,3,4],[1,4,3]]
print(paint(cost))
cost = [[1,3,2],[1,101,103],[2,3,4],[1,4,3]]
print(paint(cost))
