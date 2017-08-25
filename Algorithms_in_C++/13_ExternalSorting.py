
class Tape:
    def __init__(self):
        self.reset()
       
    def reset(self):
        self.cur = 0        
        self.body = []
        
    def read(self):
        if (self.cur >= len(self.body)):
            return None  
        return self.body[self.cur]
        
    def write(self, v):
        self.body.append(v)
        self.cur = len(self.body)-1

class LimitMem:
    def __init__(self, capacity):
        self.cap = capacity
        self.mem = [0 for i in range(self.cap)]
    
    def set(self, i, v):
        self.mem[i] = v
          
    def swap(self, i, j):
        tmp = self.mem[i]
        self.mem[i] = self.mem[j]
        self.mem[j] = tmp
              
    def upheap(self):
        self.mem.insert(0,0)
        
        i = len(self.mem)-1
        while(i != 1):
            p = i // 2
            if (self.mem[p][0] > self.mem[i][0]):
                self.swap(p, i)
            i = p
            
        self.mem.pop(0)
         
    def downheap(self, root = 1):
        self.mem.insert(0,0)
        
        count = len(self.mem)-1
        i = root
        c = i+i
        while(c <= count):
            if (c < count and self.mem[c][0] > self.mem[c+1][0]): c+= 1
            if (self.mem[i][0] > self.mem[c][0]):
                self.swap(i, c)  
                i = c
                c = i+i
            else:
                break
                
        self.mem.pop(0)
     
    def heappop(self): 
        v = self.mem[0]
        self.mem[0] = self.mem[len(self.mem)-1]
        self.mem.pop()
        self.downheap()
        return v

    def sort(self):
        count = len(self.mem)
        half = count // 2
        result = []
        for i in range(half, 0, -1):
            self.downheap(half)
        print(self.mem)    
        for i in range(count):
            result.append(self.heappop())
        
        return result         
       
def external_sort(data):
    pass

#template = list("ASORTINGANDMERGINGEXAMPLE")
template = list("ASORTINGANDM")
lmem = LimitMem(len(template))
for i in range(len(template)):
    lmem.set(i, template[i])
print(lmem.sort())

