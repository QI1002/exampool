
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

class setOfStacks:
    def __init__(self, capacity):
        self.sets = []
        self.capacity = capacity
        
    def push(self, data):
        count = len(self.sets)
        if (count == 0 or len(self.sets[count-1].body) == self.capacity):
            self.sets.append(stack())
            self.sets[count].push(data)
        else:
            self.sets[count-1].push(data)
            
    def pop(self):
        count = len(self.sets)
        if (count == 0):
            return None
        else:
            v = self.sets[count-1].pop()
            if (self.sets[count-1].isEmpty()):
                self.sets.pop()
            return v
            
mystack = setOfStacks(3)

for i in range(10):
    mystack.push(i)
    
for i in range(5):
    print(mystack.pop())
                         
for i in range(5):
    mystack.push(100+i)
    
for i in range(12):
    print(mystack.pop())
                                                 