
#460 LFU cache

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
        return self.userdata.index(i)

    def min(self):
        return None if len(self.heap) <= 1 else self.heap[1]

class lfuCache:
    def __init__(self, cap):
        self.heap = minHeap()
        self.table = {}
        self.cap = cap
        self.id = 0
        
    def getid(self):
        id = self.id
        self.id += 1
        return id
            
    def get(self, key):
        if (key in self.table):
            f = self.heap.findUserdata(key)
            self.heap.remove(f)
            self.table[key][1] = self.getid()
            self.heap.add(self.table[key][1], key)
            return self.table[key][0]
        else:
            return None
        
    def put(self, key, value):
        if (key in self.table):
            self.table[key][0] = value
            self.get(key)
        else:
            self.table[key] = [value, self.getid()]
            self.heap.add(self.table[key][1], key)            
            count = len(self.heap.heap)-1
            if (count > self.cap):
                u = self.heap.userdata[1]
                self.heap.remove()
                del self.table[u]
                 
lfu = lfuCache(2)
lfu.put(1, 2)
lfu.put(1, 3)
print(lfu.get(1))
lfu.put(2, 4)
#lfu.put(1, 5)
#print(lfu.get(1))
lfu.put(3, 4)
print(lfu.get(1))
print(lfu.get(2))


            
         