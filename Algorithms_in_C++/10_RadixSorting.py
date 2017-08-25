
import random 
import math

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

class bittype:
    def __init__(self, value):
        self.value = value
    def bits(self, index, count = 1):
        return (self.value >> index) & ((1 << count)-1)
    
def insertion_sort(data, l ,r):
    for i in range(l+1,r+1,1):    
        v = data[i] 
        j = i
        while(j >= l+1 and data[j-1] > v):
            data[j] = data[j-1]
            j -= 1
            
        data[j] = v

def raidx_straight_sort_internal(data, l, r, b, m = 1):
    mb = 1 << m
    count = len(data)
    for j in range(0,b,m):
        freq = [ 0 for i in range(mb) ] 
        temp = [ 0 for i in range(count) ]                
        for i in range(count): freq[bittype(data[i]).bits(j,m)] += 1
        for i in range(1,mb,1): freq[i] += freq[i-1]
        for i in range(count-1, -1, -1):
            freq[bittype(data[i]).bits(j,m)] -= 1
            v = freq[bittype(data[i]).bits(j,m)]            
            temp[v] = data[i]
        for i in range(count): data[i] = temp[i]
      
def raidx_straight_sort(data, m = 1):      
    count = len(data)
    l = 0
    r = count - 1
    max = data[0]
    for i in range(1, count, 1):
        if (max < data[i]):
            max = data[i]
    b = math.ceil(math.log(max, 2))
    m = 3
    raidx_straight_sort_internal(data, l ,r, b, m)
    
def radix_exchange_sort_internal(data, l ,r, b):
    if (r <= l or b < 0): return
    
    i = l
    j = r
    while(True):
        while(i <= r and bittype(data[i]).bits(b, 1) == 0): i += 1
        while(j >= l and bittype(data[j]).bits(b, 1) == 1): j -= 1
        if (i >= j): break
        swap(data, i, j)
    
    if (i > r or bittype(data[i]).bits(b, 1) == 1): i -= 1  
    
    radix_exchange_sort_internal(data, l, i, b-1)
    radix_exchange_sort_internal(data, i+1, r, b-1)

def radix_exchange_sort(data):
    count = len(data)
    l = 0
    r = count - 1
    max = data[0]
    for i in range(1, count, 1):
        if (max < data[i]):
            max = data[i]
    b = math.floor(math.log(max, 2))
    radix_exchange_sort_internal(data, l ,r, b)

def radix_exchange_sort_noRecursive(data):
    count = len(data)
    l = 0
    r = count - 1
    max = data[0]
    for i in range(1, count, 1):
        if (max < data[i]):
            max = data[i]
    b = math.floor(math.log(max, 2))
    radixstack = stack()
    
    while(True):      
        
        if (r <= l or b < 0): 
          
            if (radixstack.isEmpty()):
                break
                                  
            b = radixstack.pop()
            r = radixstack.pop()
            l = radixstack.pop()
            continue
        
        i = l
        j = r
        while(True):
            while(i <= r and bittype(data[i]).bits(b, 1) == 0): i += 1
            while(j >= l and bittype(data[j]).bits(b, 1) == 1): j -= 1
            if (i >= j): break
            swap(data, i, j)
        
        if (i > r or bittype(data[i]).bits(b, 1) == 1): i -= 1  

        radixstack.push(l)
        radixstack.push(i)
        radixstack.push(b-1)
        
        l = i+1
        b = b-1
    
sort_method = raidx_straight_sort
#sort_method = radix_exchange_sort
#sort_method = radix_exchange_sort_noRecursive

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