
#321. Create Naximun Number

class maxHeap:
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
            if (self.heap[parent] < self.heap[index]):
                self.swap(parent, index)
            else:
                break
            index = parent

    def remove(self, root = 1):
        if (len(self.heap) <= 1 or root >= len(self.heap)):
            return None
    
        parent = root
        self.swap(parent, len(self.heap)-1)
        popv = self.heap.pop()
        popu = self.userdata.pop()
        while(True):
            l = 2*parent
            r = l + 1
            max = l
            if (r < len(self.heap) and self.heap[r] > self.heap[l]):
                max = r
            if (max >= len(self.heap) or self.heap[max] <= self.heap[parent]):
                break
            self.swap(parent, max)
            parent = max
            
        return popv, popu
         
    def findUserdata(self, i):
        return self.userdata.index(i)
        
    def max(self):
        return None if len(self.heap) <= 1 else self.heap[1]

def maxofBoth(m, n, k):
    result = list(m)
    result.extend(n)
    mark = [ 0 for i in range(len(m)+len(n))]
    mh = maxHeap()
    for i in range(len(result)):
        mh.add(result[i], i)
    for i in range(k):
        v, u = mh.remove()
        mark[u] = 1        
    for i in range(len(m)+len(n)-1,-1,-1):    
        if (mark[i] == 0): result.pop(i)
        
    print(mh.heap)
    return result
    
m, n, k = [3,4,6,5], [9,1,2,5,8,3], 5
print(maxofBoth(m, n, k))    

m, n, k = [6,7], [6,0,4], 5
print(maxofBoth(m, n, k))

m, n, k = [3,9], [8,9], 3
print(maxofBoth(m, n, k))