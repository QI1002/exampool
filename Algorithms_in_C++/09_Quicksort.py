
import random 

class stack:
    def __init__(self):
        self.body = []

    def push(self, data):
        self.body.append(data)

    def pop(self):
        if (len(self.body) == 0):
            return None
        else:
            return self.body.pop()

    def isEmpty(self):
        return True if len(self.body) == 0 else False

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

def partition(data, l, r, newflow = True):
    if (r <= l): return l
      
    if (newflow and data[l] > data[r]):
        swap(data, l, r)
                
    v = data[r]  
    i = l-1
    j = r
    while(True): 
      
        while(True):
            i+= 1   
            if (data[i] >= v): break
              
        while(True):
            j-= 1 
            if (not newflow and j < l): break
            if (data[j] <= v): break
        
        #print((l,r,i,j,v,data))
        if (i >= j): break
        swap(data, i, j)
        
    swap(data, i, r)    
    return i
       

#two issues 
#1. can't sort all array with the same values (fixed)
#2. need a more check in the left
def quick_sort_internal(data, l, r, newflow):
    if (l >= r): return
      
    i = partition(data, l, r, newflow)        
    quick_sort_internal(data, l, i-1, newflow)
    quick_sort_internal(data, i+1, r, newflow)
    
def quick_sort(data, newflow = True):
    l = 0
    r = len(data)-1
    quick_sort_internal(data, l, r, newflow) 

def quick_sort_noRecursive(data, newflow = True):
    l = 0
    r = len(data)-1
    qstack = stack()
    
    while(True):      
        while(l < r):
            i = partition(data, l, r, newflow)          
            qstack.push(l)
            qstack.push(i-1)            
            l = i+1
            
        if (qstack.isEmpty()): break
        r = qstack.pop()
        l = qstack.pop()
        if (l >= r): continue
    
#use insertion sort with small partitions
def insertion_sort(data, l ,r):
    for i in range(l+1,r+1,1):    
        v = data[i] 
        j = i
        while(j >= l+1 and data[j-1] > v):
            data[j] = data[j-1]
            j -= 1
            
        data[j] = v
        
def quick_sort_internal_new(data, l, r, newflow):
    if (l >= r): return
      
    if ((r-l) < 5): 
        insertion_sort(data, l,r)
        return
            
    i = partition(data, l, r, newflow)
    quick_sort_internal_new(data, l, i-1, newflow)
    quick_sort_internal_new(data, i+1, r, newflow)
        
def quick_sort_new(data, newflow = True):
    l = 0
    r = len(data)-1
    quick_sort_internal_new(data, l, r, newflow) 
    
# k from 0 related to (l,r) but i is from l .. r 
def selectSmallK_internal(data, k, l, r):     
    i = partition(data, l, r)
    if (i == (k+l)): return data[i]
    if (i > (k+l)):
        return selectSmallK_internal(data,k,l,i-1)
    else:
        return selectSmallK_internal(data,k+l-i-1,i+1,r)

def selectSmallK(data, k):
    count = len(data)    
    if (k >= count): return None 
      
    return selectSmallK_internal(data, k, 0, count-1)
    

def selectSmallK_noRecursive(data, k):
    l = 0 
    r = len(data)-1
    if (k > r): return None 
      
    while(True):
        i = partition(data, l, r)
        if (i == (k+l)): return data[i]
        if (i > (k+l)):
            r = i-1
        else:
            k = k+l-i-1
            l = i+1

    # shall not occur in here
    return None
                
#target = genShuffleData(100)
#target = genRandomData(100, 20)
#target = [i for i in range(3, 0, -1)]
#target = [i for i in range(1,4,1)]
#target = [1, 3, 5, 4, 1, 5, 5, 4, 2, 3]
#target = [5, 5, 5]
#print(target)
#select_method = selectSmallK
#select_method = selectSmallK_noRecursive
#for i in range(len(target)):
#    print(select_method(target, i))

#sort_method = quick_sort
#sort_method = quick_sort_new
sort_method = quick_sort_noRecursive

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