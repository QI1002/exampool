
#381. Insert Delete GetRandom O(1) - Duplicates allowed

import random 
class o1c:
    def __init__(self):
        self.data = []
        
    def insert(self, val):
        self.data.append(val)
        
    def remove(self, val):
        if (val in self.data):
           self.data.remove(val)
           
    def random(self):
        count = len(self.data)
        return self.data[random.randint(0,count-1)]
        
oc = o1c()
oc.insert(2)
oc.insert(3)
oc.insert(4)
oc.insert(2)
oc.insert(3)
oc.remove(2)
for i in range(10):
    print("{0}:{1}".format(i, oc.random()))

        