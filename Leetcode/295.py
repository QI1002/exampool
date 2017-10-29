
#295. Find Median from Data Stream

class heap:
    def __init__(self):
        self.heap = [-1]

    def swap(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def add(self, v):
        self.heap.append(v)
        index = len(self.heap)-1
        while (index != 1):
            parent = index // 2
            if (self.heap[parent] > self.heap[index]):
                swap(heap, parent, index)
            else:
                break
            index = parent

    def remove(self):
        result = self.eap[1]
        tail = self.heap.pop()
        if (len(self.heap) != 1):
            parent = 1
            self.heap[parent] = tail
            while(True):
                l = 2*parent
                r = l + 1
                min = l
                if (r < len(self.heap) and self.heap[r] < self.heap[l]):
                    min = r
                if (min >= len(self.heap) or self.heap[min] >= self.heap[parent]):
                    break
                swap(parent, min)
                parent = min
        return result

class median:
    def __init__(self):
        self.heap = heap()

    def add(v):
        self.heap.add(v)

    def find():
        pass 
