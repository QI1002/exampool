
import random
import copy

def selectM(data, m):
    remain = copy.copy(data)    
    result = []
        
    count = len(data)
    if (m >= count):
        return None
          
    for i in range(count-1,0,-1):
        index = random.randint(0, i)
        result.append(remain.pop(index))
        m -= 1
        if (m == 0):
            break
            
    if (m > 0):    
        result.append(remain[0])      
          
    return result
          
print(selectM(list(range(20)), 15))