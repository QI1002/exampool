
"""
string is average 100 characters 
storage 1000 strings in DRAM

2*1000*1000*1000 bytes 
=>
20*1000*1000

read storge to sort 20*1000 group strings 
and merge sort 1000 group strings to get the sort of 1000*1000 strings (1000 strings per group)

and merge sor 20 group strings to get the sort of 20*1000*1000 strings (1000*1000 strings per group)

the total read per string is 3 times depend on your storage capacity
"""

template1 = [3,4,5,2,1]
template2 = [2,1,5,3,4]

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
    
    
print("sort {0} = {1}".format(template1, heap_sort(template1)))
print("sort {0} = {1}".format(template2, heap_sort(template2)))
