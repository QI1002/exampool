
import random 

class poker:
    def __init__(self):
        self.kinds = ['clubs', 'diamonds', 'hearts', 'spade']        
        self.cards = [i for i in range(52)]
    
    def show(self, i):
        if (i >= len(self.cards)):
            return ""
        return self.kinds[i%4] + " " + str((i//4)+1)
        
    def shuffle(self):
        remain = [i for i in range(52)]
        result = []
        for i in range(51,0,-1):
            index = random.randint(0, i)
            result.append(remain.pop(index))
        result.append(remain[0])    
            
        self.cards = result
        return result
        
    def showall(self):
        for i in range(52):
            print("{0}:{1}".format(self.cards[i], self.show(self.cards[i])))
        
        
p = poker()
print(p.shuffle())
p.showall()