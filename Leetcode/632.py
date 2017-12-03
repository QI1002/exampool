
#632. Smallest Range

def getMin(a,b,c):
    if (a > b):
        min = b if (c > b) else c
    else:
        min = a if (c > a) else c
    
    return min

def getMax(a,b,c):
    if (a > b):
        max = a if (a > c) else c 
    else:
        max = b if (b > c) else c 
    
    return max
        
def getRange(a, b, c):
    max = getMax(a, b, c)
    min = getMin(a, b, c)
    
    return (max-min) 
            
def smallestRange(data):

    idx = []
    rr = None               
    ai = all = 0
    r = -1            
    for x in data:
        idx.append(0)
        all += len(x)  
                    
    while (ai != (all-len(data))):

        min = max = data[0][idx[0]]        
        for i in range(1,len(data),1):
            if (min > data[i][idx[i]]): min = data[i][idx[i]]
            if (max < data[i][idx[i]]): max = data[i][idx[i]]

        print((max,min,idx,r))
        if (r == -1 or (max-min) < r): 
            r = max-min
            rr = (max, min)
            
        jj = j = -1
        for i in range(len(data)):
            if ((idx[i]+1) == len(data[i])):
                continue
            if (jj == -1 or jj > data[i][idx[i]]):
                jj = data[i][idx[i]]
                j = i    
                 
        ai += 1
        idx[j] += 1
    
    return rr 

data1 = [4,10,15,24,26]
data2 = [0,9,12,20]
data3 = [5,18,22,30]
data = [data1, data2, data3]
print(smallestRange(data))