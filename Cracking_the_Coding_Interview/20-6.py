
import random 

def swap(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp
    
def heap_add(heap, v):
    heap.append(v)
    index = len(heap)-1
    while (index != 1):
        parent = index // 2
        if (heap[parent] > heap[index]):
            swap(heap, parent, index)
        else:
            break    
        index = parent    
    
def heap_remove(heap):
    result = heap[1]
    tail = heap.pop()
    if (len(heap) != 1):
        parent = 1
        heap[parent] = tail    
        while(True):
            l = 2*parent
            r = l + 1
            min = l
            if (r < len(heap) and heap[r] < heap[l]):
                min = r 
            if (min >= len(heap) or heap[min] >= heap[parent]):        
                break
            swap(heap, parent, min)    
            parent = min    
    return result                        
    
def heap_sort(ll):
    # dummy item in index = 0
    heap = [-1]
    result = [] 
    for i in range(len(ll)):
        heap_add(heap, ll[i])
    #print(heap)    
    for i in range(len(ll)):
        result.append(heap_remove(heap))
        print(heap)
        
    return result    
    
def findMaxN(maxN, data):
    heap = [-1]
    result = []
    for i in range(len(data)):
        heap_add(heap, data[i])
        if (len(heap) > (maxN+1)):
            heap_remove(heap)
    #print(heap)
        
    for i in range(maxN):
        result.append(heap_remove(heap))

    #print(heap)
        
    return result    

def shuffle(n):
    result = []
    remain = [i for i in range(1,n+1,1)]
    for i in range(n-1, -1, -1):
        index = random.randint(0, i)    
        result.append(remain.pop(index))
        
    return result
    
#print(len(shuffle(10000)))
print(findMaxN(100, shuffle(10000)))
    
    