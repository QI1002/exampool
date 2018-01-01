
#699. Falling Squares

class fallingSquare:

    def __init__(self):
        self.pos = {} 

    def addSquare(self, start, h):
        self.pos[0] = 0
        base = 0   
        for i in range(start, start+h, 1):
            if (i in self.pos and self.pos[i] > base):
                base = self.pos[i]
        for i in range(start, start+h, 1):
                self.pos[i] = base + h

    def getHeight(self):
        hi = -1
        for k in self.pos:
            if (hi == -1 or self.pos[hi] < self.pos[k]):
                hi = k
        return self.pos[hi]

seq = [[1,2], [2,3], [6,1]]
fs = fallingSquare()

for i in range(len(seq)):
    fs.addSquare(*seq[i])
    print(fs.getHeight())

