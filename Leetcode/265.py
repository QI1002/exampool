
#256. Paint House 

class stack:
    def __init__(self):
        self.body = []

    def push(self, data):
        self.body.append(data)

    def pop(self):
        if (len(self.body) == 0):
            return None
        else:
            return self.body.pop()

    def isEmpty(self):
        return True if len(self.body) == 0 else False

def paint(cost):
    n = len(cost)
    k = len(cost[0])
    min1s = []
    min2s = []

    min1 = min2 = 0
    i1 = i2 = -1
    for i in range(n):
        m1 = m2 = None
        t1 = t2 = None
        for j in range(k):
            v = cost[i][j] + (min2 if (j == i1) else min1)
            t = list(min2s) if (j == i1) else list(min1s)
            if (m1 == None or m1 > v):
                m2,i2,t2 = m1,i1,t1
                m1,i1,t1 = v,j,t
            else: 
                if (m2 == None or m2 > v) : 
                    m2,i2,t2 = v,j,t

        min1s = t1
        min2s = t2
        min1s.append(i1)
        min2s.append(i2)
        min1 = m1 
        min2 = m2

    return min1, min1s  


cost = [[1,3,2,4],[4,1,2,3],[2,3,1,4],[1,4,2,3]]
print(paint(cost))
cost = [[1,3,2,4],[1,101,102,103],[2,3,1,4],[1,4,2,3]]
print(paint(cost))
