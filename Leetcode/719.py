
#719. Find K-th Smallest Pair Distance

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

    def num(self):
        return len(self.heap)-1

    def max(self):
        return None if len(self.heap) <= 1 else self.heap[1]

def keepK(mh, v, k):
    mh.add(v)
    if (mh.num() > k):
        mh.remove()

def smallDist(data, k):
    d0 = sorted(data)
    ddd = [ d0 ]
    count = len(data)
    mh = maxHeap()
    for i in range(1, count, 1):
        dd = []
        for j in range(i, count, 1):
            dd.append(d0[j]-d0[j-i])
        dds = sorted(dd)
        ddd.append(dds)
        for x in dds:
            if (mh.num() < k or mh.max() > x): 
                keepK(mh, x, k)
        if (i == k): break

    print(ddd)
    
    return mh.max()

for j in range(1,7,1):
    print(smallDist([1,2,3,6], j))
    
