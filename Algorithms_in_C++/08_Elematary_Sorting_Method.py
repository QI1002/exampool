
import random 

def swap(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp

def genRandomData(n, m):
    result = []
    while(n > 0):        
        result.append(random.randint(1, m))
        n -= 1
    return result

def genShuffleData(n):
    result = []
    remain = [i for i in range(1,n+1,1)]
    for i in range(n-1, -1, -1):
        index = random.randint(0, i)
        result.append(remain.pop(index))
    return result
        
def selection_sort(data):
    count = len(data)    
    for i in range(count):
        min = i
        for j in range(i+1, count, 1):
            if (data[min] > data[j]):
                min = j
        swap(data, min, i)          
    
def switch_sort_indirect(data, indirect):
    count = len(data)    
    for i in range(count):
        v = data[i]
        j = i
        n = indirect[j]
        while(n != i):
            #print((i,j,n))          
            data[j] = data[n]            
            t = j
            j = n            
            n = indirect[j]
            indirect[t] = t
                    
        data[j] = v
        indirect[j] = j
    
def selection_sort_indirect(data):    
    count = len(data)
    indirect = [i for i in range(count)]
    for i in range(count):
        min = i
        for j in range(i+1, count, 1):
            if (data[indirect[min]] > data[indirect[j]]):
                min = j     
        swap(indirect, min, i) 
    
    #print(indirect)
    switch_sort_indirect(data, indirect)
            
def insertion_sort(data, h = 1):
    count = len(data)    
    for i in range(h,count,1):    
        v = data[i] 
        j = i
        while(j >= h and data[j-h] > v):
            data[j] = data[j-h]
            j -= h
            
        data[j] = v

def bubble_sort(data):
    count = len(data)    
    for i in range(count, -1, -1):
        for j in range(1, count, 1):
            if (data[j-1] > data[j]):
                swap(data, j-1, j)
          
def shell_sort(data):
    
    count = len(data)
    h = 1
    while(h <= count/9): h = 3*h + 1
    
    while(h > 0):  
        insertion_sort(data, h)
        h //= 3
        
def distributive_sort(data):
    m = data[0]
    count = len(data)
    for i in range(count):
        if (data[i] > m):
            m = data[i]
                
    freq = [ 0 for i in range(m+1) ] 
    temp = [ 0 for i in range(count) ]           
    for i in range(count): freq[data[i]] += 1
    for i in range(1,m+1,1): freq[i] += freq[i-1]
    for i in range(count-1, -1, -1):
        freq[data[i]] -= 1
        temp[freq[data[i]]] = data[i]
    for i in range(count): data[i] = temp[i]

#sort_method = selection_sort
#sort_method = insertion_sort
#sort_method = bubble_sort
#sort_method = shell_sort
#sort_method = distributive_sort
sort_method = selection_sort_indirect

target1 = genShuffleData(100)
target2 = genRandomData(100, 20)
target3 = [i for i in range(20, 0, -1)]
target4 = [i for i in range(1,21,1)]
target5 = [5 for i in range(20)]
target6 = [1, 3, 5, 4, 1, 5, 5, 4, 2, 3]
targets = [target1, target2, target3, target4, target5, target6]

for i in range(len(targets)):
    print(targets[i])
    sort_method(targets[i])
    print(targets[i])
    print("=================================")