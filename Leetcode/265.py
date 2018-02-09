
#265. Paint House II 

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
    mins = []
    result = []

    maxi = maxgap = None
    for i in range(n):
        min1 = min2 = None
        for j in range(k):
            if (min1 == None or cost[i][min1] > cost[i][j]):
                min2 = min1
                min1 = j
            else: 
                if (min2 == None or cost[i][min2] > cost[i][j]):
                    min2 = j

        if (maxgap == None or maxgap < (cost[i][min2] - cost[i][min1])):
            maxgap = cost[i][min2] - cost[i][min1]
            maxi = i

        mins.append((min1,min2))
    
    result.append(mins[maxi][0])
    prev = mins[maxi][0]
    for i in range(maxi+1,n,1):
        min1, min2 = mins[i]
        prev = min1 if (prev != min1) else min2 
        result.append(prev)

    prev = mins[maxi][0]
    for i in range(maxi-1,-1,-1):
        min1, min2 = mins[i]
        prev = min1 if (prev != min1) else min2 
        result.insert(0, prev)

    return result  


cost = [[1,3,2,4],[4,1,2,3],[2,3,1,4],[1,4,2,3]]
print(paint(cost))
cost = [[1,3,2,4],[1,101,102,103],[2,3,1,4],[1,4,2,3]]
print(paint(cost))
