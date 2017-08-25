
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

def merge_sort_internal(source):
    count = len(source)
    if (count == 1): return source
      
    result = []      
    m = count//2
    left = merge_sort_internal(source[0:m])
    right = merge_sort_internal(source[m:])
        
    if (left[len(left)-1] < right[len(right)-1]):
        max = right[len(right)-1]+1
    else:
        max = left[len(left)-1]+1
            
    left.append(max)
    right.append(max)
    
    i = j = 0
    for k in range(count):
        if (left[i] > right[j]): 
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    
    return result
       
def merge_sort_internal_new(source):
    count = len(source)
    if (count == 1): return source
      
    result = []      
    m = count//2
    left = merge_sort_internal_new(source[0:m])
    right = merge_sort_internal_new(source[m:])
    left.extend(right[::-1])
    
    i = 0
    j = len(left)-1
    for k in range(len(left)):
        if (left[i] > left[j]): 
            result.append(left[j])
            j -= 1
        else:
            result.append(left[i])
            i += 1
    
    return result
           
def merge_sort_internal_new_noRecursive(source):
  
    mergestack = stack()
    resultstack = stack()
        
    count = len(source)
    if (count == 1): return source

    mergestack.push(source)       
    while(not mergestack.isEmpty()):
        v = mergestack.pop()
        if (v != 0):
            source = v
            count = len(source)
            if (count == 1):
                resultstack.push([source[0]])
            else:
                m = count//2    
                mergestack.push(0)       
                mergestack.push(source[m:]) 
                mergestack.push(source[0:m])
                
            continue
            
        left = resultstack.pop()
        right = resultstack.pop()
        result = []             
        left.extend(right[::-1]) 
        i = 0
        j = len(left)-1
        for k in range(len(left)):
            if (left[i] > left[j]): 
                result.append(left[j])
                j -= 1
            else:
                result.append(left[i])
                i += 1    

        resultstack.push(result) 
           
    return resultstack.pop()    
               
def merge_sort(data):
    result = merge_sort_internal(data)
    for i in range(len(data)):
        data[i] = result[i]
   
def merge_sort_new(data):
    result = merge_sort_internal_new(data)
    for i in range(len(data)):
        data[i] = result[i]
    
def merge_sort_new_noRecursive(data):
    result = merge_sort_internal_new_noRecursive(data)
    for i in range(len(data)):
        data[i] = result[i]
 
def merge_sort_new_bottomup(data):
    count = len(data)
    if (count == 1): return source
            
    h = 1
    while(h < count):
        n = h+h
        for l in range(0, count, n):
          
            if ((l+h) >= count):
                continue
                
            source = data[l:l+h]
            source.extend(data[l+n-1:l+h-1:-1])
            i = 0
            j = len(source)-1
            for k in range(l, l+len(source), 1):
                if (source[i] > source[j]): 
                    data[k] = source[j]
                    j -= 1
                else:
                    data[k] = source[i]
                    i += 1
            
        h = n

     
#sort_method = merge_sort
#sort_method = merge_sort_new
#sort_method = merge_sort_new_noRecursive
sort_method = merge_sort_new_bottomup

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