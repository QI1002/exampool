
#346. Moving Average from Data Stream 

class MovingAverage:

    def __init__(self, it, m):
        self.it = it
        self.m = m
        self.q = []
        self.s = 0
        self.acc = 0

    def next(self):

        n = None
        try: 
            n = self.it.next()
            self.acc += 1
        except StopIteration: pass

        if (self.acc > self.m):
            self.s -= self.q.pop(0)
        
        if (n != None):
            self.q.append(n)
            self.s += n

        if (len(self.q) == 0): 
            raise StopIteration
        
        return float(self.s)/len(self.q)

    def doAll(self):
        result = []
        while(True):
            try: 
                result.append(self.next())
            except StopIteration: 
                break

        return result


given, m = [1,10,3,5], 3
mavg = MovingAverage(iter(given), m)
print(mavg.doAll())






