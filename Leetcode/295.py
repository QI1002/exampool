
#295. Find Median from Data Stream

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

class median:
    def __init__(self):
        self.less = minHeap()
        self.more = minHeap()
        self.data = []

    def add(self, v):
        self.data.append(v)
        less_min = self.less.min()
        if (less_min != None and -v > self.less.min()):
            self.less.add(-v)
        else:
            self.more.add(v)

        if (len(self.more.heap) > (len(self.less.heap)+1)):
            v = self.more.min()
            self.more.remove()
            self.less.add(-v)
            
        if (len(self.less.heap) > len(self.more.heap)):
            v = self.less.min()
            self.less.remove()
            self.more.add(-v)
         
        #print((self.more.heap[1:], self.less.heap[1:]))
         
    def getMedian(self):
        if ((len(self.data) & 0x1) != 0):
            return self.more.min()
        else:
            return (-self.less.min(), self.more.min())

sample = [1,3,-1,-3,5,3,6,7]
m = median()
for i in range(len(sample)):
    m.add(sample[i])
    print("{0} median is {1}".format(m.data, m.getMedian()))