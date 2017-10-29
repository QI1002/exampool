
#239. Sliding Window Maximum

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
            return
    
        parent = root
        self.swap(parent, len(self.heap)-1)
        self.heap.pop()
        self.userdata.pop()
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

    def findUserdata(self, i):
        return self.userdata.index(i)
        
    def max(self):
        return None if len(self.heap) <= 1 else self.heap[1]

def slidingMax(data, k):
    result = []
    count = len(data)
    for i in range(count-k+1):
        l = sorted(data[i:i+k])
        result.append(l[-1])

    return result

def slidingMax2(data, k):
    def slidingPush(q, v):
        skip = 0
        while(len(q) > 0 and v > q[-1][0]):
            t = q.pop()
            skip += (t[1]+1)
        q.append([v, skip])
    def slidingPop(q):
        if (len(q) > 0):
            if (q[0][1] > 0): q[0][1] -= 1
            else: q.pop()
    def slidingMax(q):
        return q[0][0]

    q = []
    result = []
    count = len(data)
    for i in range(count):
        slidingPush(q, data[i])
        if (i < (k-1)): continue
        result.append(slidingMax(q))
        slidingPop(q)

    return result

def slidingMax3(data, k):
    mp = maxHeap()
    result = []
    count = len(data)
    j = 0
    for i in range(count):
        mp.add(data[i], i)
        if (i < (k-1)): continue
        result.append(mp.max())
        jj = mp.findUserdata(j)         
        mp.remove(jj)        
        #print((data[jj], j, jj))
        j += 1

    return result
    
sample, kk = [1,3,-1,-3,5,3,6,7], 3
print(slidingMax(sample, kk))
print(slidingMax2(sample, kk))
print(slidingMax3(sample, kk))

sample, kk = [1,3,-1,-3,5,3,6,7], 5
print(slidingMax(sample, kk))
print(slidingMax2(sample, kk))
print(slidingMax3(sample, kk))