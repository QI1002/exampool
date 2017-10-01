
#146. LRU cache

class LRUCache:
    def __init__(self, cap = 3):
        self.cache = {}
        self.stamps = {}
        self.cap = cap
        self.stamp = 0
        
    def findLRU(self):
        LRUKey = -1
        for key in self.stamps:
            if (LRUKey == -1):
                LRUKey = key
                continue
            
            if (self.stamps[LRUKey] > self.stamps[key]):
                LRUKey = key          
                
        return LRUKey
            
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
            
        self.stamp += 1
        self.stamps[key] = self.stamp
        self.cache[key] = value
            
    def get(self, key):
        if (not key in self.cache):
            return None
        else:    
            self.stamp += 1
            self.stamps[key] = self.stamp
            return self.cache[key]
        
        
cache = LRUCache()
cache.put("a", 1)
cache.put("b", 2)
cache.put("c", 3)
print(cache.get("a"))
cache.put("d", 4)
print((cache.cache, cache.stamps))
