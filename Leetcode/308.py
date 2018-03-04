
#308. Range Sum Query 2D - Mutable

class matrixSum:

    def __init__(self, m):
        self.m = m 
        self.rowc = len(m)
        self.colc = len(m[0])
        self.rr = self.accSum()
        print(self.rr)

    def accSum(self): 

        r = [ 0 for i in range(self.colc) ]
        rr = [ list(r) for i in range(self.rowc) ] 

        rr[0][0] = self.m[0][0]
        for i in range(1, self.colc):
            rr[0][i] = rr[0][i-1] + self.m[0][i]

        for j in range(1, self.rowc):
            rr[j][0] = rr[j-1][0] + self.m[j][0]
            for i in range(1, self.colc):
                rr[j][i] = rr[j][i-1] + rr[j-1][i] - rr[j-1][i-1] + self.m[j][i]

        return rr

    def checkXY(self, x, y):
        if (x < 0 or x >= self.colc): raise ValueError("wrong parameter")
        if (y < 0 or y >= self.rowc): raise ValueError("wrong parameter")

    def partialSum(self,t,l,b,r):
       
        self.checkXY(l, t)
        self.checkXY(r, b)
        s = self.rr[b][r]
        if (t != 0): s -= self.rr[t-1][r]
        if (l != 0): s -= self.rr[b][l-1]
        if (t != 0 and l != 0): s += self.rr[t-1][l-1]
        return s

    def update(self,y,x,v):
       
        self.checkXY(x, y)
        oldv = self.m[y][x]
        self.m[y][x] = v
        d = v - oldv
        for j in range(y, self.rowc):
            for i in range(x, self.colc): 
                self.rr[j][i] += d 

given = [[3,0,1,4,2],
         [5,6,3,2,1],
         [1,2,0,1,5],
         [4,1,0,1,7],
         [1,0,3,0,5]]  

ms = matrixSum(given)
print(ms.partialSum(2,1,4,3))
print(ms.partialSum(0,0,4,3))
print(ms.partialSum(2,0,4,3))
print(ms.partialSum(0,1,4,3))
ms.update(3,2,2)
print(ms.partialSum(2,1,4,3))

