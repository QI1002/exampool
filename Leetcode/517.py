
#517. Super Washing Machines

def getDiff(data, s):
    return [ data[i]-s for i in range(len(data)) ]
    
def moveWashMach(data):
    count = len(data)
    sum = 0
    for i in range(count):
        sum += data[i]
    
    if ((sum % count) != 0):
        return None 
    
    step,md = 0, 1
    s = sum//count
    print((step, data))        
    while(md != 0):
    
        md, mm, mi = 0, -1, -1
        d = getDiff(data, s)
        for i in range(len(d)):
           if (d[i] > 0 and mi == -1): mm, mi = d[i], i        
           if (abs(d[i]) > md): md = abs(d[i])
           
        j = -1
        i = mi-1   
        while(i >= 0):
            if (data[i] == 0): break
            if (d[i] < 0): j = i
            i -= 1
             
        if (i >= 0 or j != -1):
            if (i < 0): i = j
            data[i] += 1
            data[mi] -= 1
            step += 1                
            #print((step, data, mi, i, d))
            print((step, data))
            continue
            
        j = -1  
        i = mi+1  
        while(i < len(data)):
            if (data[i] == 0): break
            if (d[i] < 0): j = i
            i += 1
            
        if (i < len(data) or j != -1):
            if (i >= len(data)): i = j
            data[i] += 1
            data[mi] -= 1    
            step += 1            
            #print((step, data, mi, i, d))
            print((step, data))
            continue
    
    return step
         
    
#print(moveWashMach([1,0,5]))        
#print(moveWashMach([5,0,1]))        
#print(moveWashMach([1,0,4,0,5]))             
#print(moveWashMach([5,0,4,0,1]))             
print(moveWashMach([2,0,5,0,3]))             