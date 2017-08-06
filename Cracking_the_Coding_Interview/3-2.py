
class stack:
    def __init__(self):
        self.body = []
    
    def push(self, data):
        minValue = self.min()
        if (minValue == None or data < minValue):
            minValue = data
        self.body.append((data, minValue))
            
    def pop(self):
        if (len(self.body) == 0):
            return None
        else:    
            return self.body.pop()[0]

    def min(self):
        if (len(self.body) == 0):
            return None
        else:    
            v = self.body.pop()
            self.body.append(v)
            return v[1]
        
values = [ 3, 5, 2, 1, 4 ]
minstack = stack()
for i in range(len(values)):
    minstack.push(values[i])
    print("after push {0}, the min value = {1}".format(values[i], minstack.min()))
    
for i in range(len(values)):
    v = minstack.pop()
    print("after pop {0}, the min value = {1}".format(v, minstack.min()))
    
               
    