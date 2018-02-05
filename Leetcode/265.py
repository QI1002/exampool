
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
    order = []
    
    for i in range(n):
        t = sorted(range(k), key = lambda j: cost[i][j])
        order.append(t)

    print(order)
    index = [0,0,0,0]
    while(True):
       result = [ order[i][index[i]] for i in range(n) ]
       conflict = False
       for i in range(1, n, 1):
           if (result[i] == result[i-1]):
               conflict = True
               break 
       if (conflict == False): break    

    return result           
            
 

cost = [[1,3,2,4],[4,1,2,3],[2,3,1,4],[1,4,2,3]]
print(paint(cost))
