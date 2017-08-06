

class stack:
    def __init__(self, array, start, end):
        self.array = array
        self.start = start
        self.top = start-1
        self.end = end
    
    def push(self,data):
        if (self.top >= self.end):
            return False
        else:                
            self.top += 1
            self.array[self.top] = data
            return True
            
    def pop(self):
        if (self.top < self.start): 
            return None
        else:    
            index = self.top
            self.top -= 1
            return self.array[index]
            
arraylist = []
for i in range(30):
    arraylist.append(0)
                
stack0 = stack(arraylist, 0, 9)                
stack1 = stack(arraylist, 10, 19)
stack2 = stack(arraylist, 20, 29)
        
for i in range(12):
    stack0.push(i)
    stack1.push(i+10)
    stack2.push(i+20)
    
for i in range(11):
    print(stack0.pop())        
    print(stack1.pop())
    print(stack2.pop())