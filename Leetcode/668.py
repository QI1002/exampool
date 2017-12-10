
#668. Kth Smallest Number in Multiplication Table

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

def smallK(m, n, k):
    count = 0
    h = maxHeap()
    for i in range(m):
        for j in range(n):
            h.add((i+1)*(j+1))
            count += 1
            if (count > k):
                h.remove() 
 
    return h.max()

print(smallK(3,3,5))
print(smallK(2,3,6))
