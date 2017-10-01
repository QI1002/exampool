
#146. LRU cache

class LRUCache:
    def __init__(self, cap = 3):
        self.cache = {}
        self.stamps = {}
        self.heap = [0]
        self.cap = cap
        self.stamp = 0
        
    def findLRU2(self):
        LRUKey = -1
        for key in self.stamps:
            if (LRUKey == -1):
                LRUKey = key
                continue
            
            if (self.stamps[LRUKey] > self.stamps[key]):
                LRUKey = key          
                
        return LRUKey
         
    def swapHeap(self, a, b):
        tmp = self.heap[a]
        self.heap[a] = self.heap[b]      
        self.heap[b] = tmp
        
    def updateLRU(self, key):
        i = self.heap.index(key)
        while(True):
            c = i+i
            if ((c+1) < len(self.heap) and 
                self.stamps[self.heap[c]] > self.stamps[self.heap[c+1]]):
                c += 1
            if (c < len(self.heap) and 
                self.stamps[self.heap[i]] > self.stamps[self.heap[c]]): 
                self.swapHeap(c, i)
            else:
                break

            i = c                  
            
    def findLRU(self):
        return self.heap[1]
                                    
    def updateStamp(self, key):
        self.stamp += 1
        self.stamps[key] = self.stamp
        self.updateLRU(key)

    def isFull(self):
        return len(self.cache) == self.cap
        
    def put(self, key, value):
    
        if (self.get(key) != None):
            self.cache[key] = value
            return
            
        if (self.isFull()):
            rKey = self.findLRU()
            del self.cache[rKey]
            del self.stamps[rKey]
            self.heap[1] = key
        else:    
            self.heap.append(key)
            
        self.updateStamp(key)
        self.cache[key] = value
            
    def get(self, key):
        if (not key in self.cache):
            return None
        else:    
            self.updateStamp(key)
            return self.cache[key]
        
        
cache = LRUCache()
cache.put("a", 1)
cache.put("b", 2)
cache.put("c", 3)
print(cache.get("a"))
cache.put("d", 4)
print((cache.cache, cache.stamps))
cache.put("e", 5)
print((cache.cache, cache.stamps))
cache.put("f", 6)
print((cache.cache, cache.stamps))
