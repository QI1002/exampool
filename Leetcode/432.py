
#432. All O'one Data Structure

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

    def removeBy(self, u):
        r = self.findUserdata(u)
        if (r != None): self.remove(r)
        
    def min(self):
        return None if len(self.heap) <= 1 else self.heap[1]

class allOone:
    def __init__(self):
        self.maxheap = minHeap()
        self.minheap = minHeap()
        self.hash = {}
        
    def inc(self, key):
        if (not key in self.hash):
            self.hash[key] = 0
            self.maxheap.add(-key, key)
            self.minheap.add(key, key)
        self.hash[key] += 1
        
    def dec(self, key):
        if (not key in self.hash):
            return        
        self.hash[key] -= 1
        if (self.hash[key] == 0):
            del self.hash[key] 
            self.maxheap.removeBy(key)
            self.minheap.removeBy(key)
            
    def getMaxKey(self):
        r = self.maxheap.min()
        return -r if r != None else None 
        
    def getMinKey(self):
        return self.minheap.min()
        
        
aoo = allOone()
aoo.inc(1)
aoo.inc(1)
aoo.inc(2)
aoo.inc(3)
aoo.dec(1)            
print((aoo.hash, aoo.getMaxKey(), aoo.getMinKey()))
aoo.dec(1)
print((aoo.hash, aoo.getMaxKey(), aoo.getMinKey()))
aoo.dec(1)
print((aoo.hash, aoo.getMaxKey(), aoo.getMinKey()))
aoo.dec(3)
print((aoo.hash, aoo.getMaxKey(), aoo.getMinKey()))