
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
    
def findMedian(data):

    lessheap = [-1]
    moreheap = [-1]

    if (len(data) == 1): 
        return data[0]
    else:  
        heap_add(lessheap, -(data[0] if data[0] < data[1] else data[1]))
        heap_add(moreheap, (data[1] if data[0] < data[1] else data[0]))
              
    for i in range(2, len(data), 1):
        
        l = -lessheap[1]
        r = moreheap[1]
        print((data[i],l,r))           
        if (data[i] < l): 
            heap_add(lessheap, -data[i])
        else: 
            if (data[i] > r): 
                heap_add(moreheap, data[i])          
            else:
                heap_add(moreheap, data[i])
          
        lesslen = len(lessheap)
        morelen = len(moreheap)
        if (morelen > (lesslen+1)):
            more = heap_remove(moreheap)
            heap_add(lessheap, -more)        
        if (lesslen > (morelen+1)):
            less = -heap_remove(lessheap)
            heap_add(moreheap, less)           

    lesslen = len(lessheap)
    morelen = len(moreheap)
    if (lesslen > morelen): return -heap_remove(lessheap)
    if (morelen > lesslen): return heap_remove(moreheap)
    return (-heap_remove(lessheap), heap_remove(moreheap))

def shuffle(n):
    result = []
    remain = [i for i in range(1,n+1,1)]
    for i in range(n-1, -1, -1):
        index = random.randint(0, i)    
        result.append(remain.pop(index))
        
    return result
    
print(findMedian(shuffle(899)))
    
    