
#480. Sliding Window Median

class minHeap:
    def __init__(self):
        self.heap = [-1]
        self.userdata = [-1]

    def swap(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp
        tmp = self.userdata[i]
        self.userdata[i] = self.userdata[j]
        self.userdata[j] = tmp

    def add(self, v, u = None):
        self.heap.append(v)
        self.userdata.append(u)
        index = len(self.heap)-1
        while (index != 1):
            parent = index // 2
            if (self.heap[parent] > self.heap[index]):
                self.swap(parent, index)
            else:
                break
            index = parent

    def remove(self, root = 1):
        if (len(self.heap) <= 1 or root >= len(self.heap)):
            return

        parent = root
        self.swap(parent, len(self.heap)-1)
        self.heap.pop()
        self.userdata.pop()
        while(True):
            l = 2*parent
            r = l + 1
            min = l
            if (r < len(self.heap) and self.heap[r] < self.heap[l]):
                min = r
            if (min >= len(self.heap) or self.heap[min] >= self.heap[parent]):
                break
            self.swap(parent, min)
            parent = min

    def findUserdata(self, i):
        if (i in self.userdata):
            return self.userdata.index(i)
        else:
            return None    

    def min(self):
        return None if len(self.heap) <= 1 else self.heap[1]

class median:
    def __init__(self, k):
        self.k = k
        self.id = 0
        self.less = minHeap()
        self.more = minHeap()
        self.data = []

    def getid(self):
        id = self.id
        self.id += 1
        return id

    def update(self):
        if (len(self.more.heap) > (len(self.less.heap)+1)):
            v = self.more.min()
            u = self.more.userdata[1]
            self.more.remove()
            self.less.add(-v, u)
            
        if (len(self.less.heap) > len(self.more.heap)):
            v = self.less.min()
            u = self.less.userdata[1]
            self.less.remove()
            self.more.add(-v, u)
         
        print((self.more.heap[1:], self.less.heap[1:]))
            
    def add(self, v):
        self.data.append(v)
        less_min = self.less.min()
        u = self.getid()
        if (less_min != None and -v > self.less.min()):
            self.less.add(-v, u)
        else:
            self.more.add(v, u)
            
        self.update()
         
    def remove(self):
        self.data.pop(0)
        u = self.id - self.k        
        
        f = self.less.findUserdata(u) 
        if (f != None): self.less.remove(f)
        f = self.more.findUserdata(u) 
        if (f != None): self.more.remove(f)
        
        self.update()
        
    def getMedian(self):
        if ((self.k & 0x1) != 0):
            return self.more.min()
        else:
            return (-self.less.min(), self.more.min())

def slidingMedian(data, k):
    m = median(k)
    mm = []
    for i in range(len(data)):
        m.add(data[i])
        if ((i+1) >= k):
            mm.append(m.getMedian())    
            m.remove()
    return mm    

def slidingMedian2(data, k):
    mm = []
    count = len(data)
    for i in range(count-k+1):
        m = sorted(data[i:i+k])
        if ((k & 1) != 0):
            mm.append(m[k//2])
        else:
            mm.append((m[k//2-1], m[k//2]))
    return mm
 
sample = [1,3,-1,-3,5,3,6,7]
print(slidingMedian2(sample, 3)) 
print(slidingMedian(sample, 3)) 
