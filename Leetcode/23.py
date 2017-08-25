
#23. Merge k Sorted Lists
#I1. downheap lose break condition
#I2. 

def swap(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp
    
def upheap(heap):
    i = len(heap)-1
    while(i != 1):
        p = i // 2
        if (heap[p][0] > heap[i][0]):
            swap(heap, p, i)
        i = p

def downheap(heap):
    count = len(heap)-1
    i = 1
    c = i+i
    while(c <= count):
        if (c < count and heap[c][0] > heap[c+1][0]): c+= 1
        if (heap[i][0] > heap[c][0]):
            swap(heap, i, c)  
            i = c
            c = i+i
        else:
            break    
                  
def mergeSorts(sorts):
    count = len(sorts)
    index = [0 for i in range(count)]
    heap = [0]
    max = 0
    allcount = 0
    
    for i in range(count):
        allcount += len(sorts[i])
        if (max < sorts[i][len(sorts[i])-1]):
            max = sorts[i][len(sorts[i])-1]             
    
    max += 1
    for i in range(count):
        sorts[i].append(max)
        heap.append((sorts[i][0], i))
        upheap(heap)        
        
    result = []            
    for j in range(allcount):
        v = heap[1]
        result.append(v[0])
        i = v[1]
        index[i] += 1
        heap[1] = (sorts[i][index[i]], i)
        downheap(heap)
                              
    for i in range(count):
        sorts[i].pop()
              
    return result
    
sort1 = [1,3,6]
sort2 = [3,7,8]
sort3 = [0,1,2]
sort4 = [5,9,10]
sort5 = [2,3,9]

sorts = [sort1, sort2, sort3, sort4, sort5]
print(mergeSorts(sorts))