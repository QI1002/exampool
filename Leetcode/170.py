
#170. Two Sym III- Data strcuture design 

class PairSum:
    def __init__(self):
        self.data = []

    def add(self, v):
        i = 0
        while (i < len(self.data) and self.data[i] < v): i += 1
        self.data.insert(i, v)
  
    def find(self, v):
        result = []
        i = 0
        while (i < len(self.data) and self.data[i] < v//2): i += 1
        if (i == len(self.data)): return result
        if (self.data[i] != v//2): i -= 1
        for j in range(0,i+1,1):
            sv = v - self.data[j]
            if (sv in self.data[i+1:]):
                result.append((self.data[j], sv))
        return result

PS = PairSum()
PS.add(7)
PS.add(11)
PS.add(15)
PS.add(2)
print("{0}=>{1}".format(PS.data, PS.find(9)))

