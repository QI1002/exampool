
#327. Count of Range Sum

def countRangeAdd(t, result, upper, lower):
    if (t[2] >= lower and t[2] <= upper): 
        result.append(t)
     
def countRangeSum(data, upper, lower):

    count = len(data)
    result = []
    
    base1 = [ [(i,i,data[i])] for i in range(count) ]
    for x in base1: countRangeAdd(x[0], result, upper, lower)
    
    while(len(base1) > 1):
    
        base2 = []
        for i in range(0, (len(base1)//2)*2, 2):
            base = []
            start = i
            end = i+1
            
            base.extend(base1[start])
            base.extend(base1[end])
            for x in base1[start]:
                for y in base1[end]:
                    if ((x[1]+1) != y[0]):  continue
                    base.append((x[0],y[1],x[2]+y[2]))            
                    countRangeAdd(base[-1], result, upper, lower)
                    
            #print((start, end, base))
            base2.append(base)
            
        if ((len(base1) & 0x1) != 0): base2.append(base1[-1])                        
        #print((base1, base2))
        base1 = base2 
        
    return result
    
sample = [-2,5,-1]
print(countRangeSum(sample, 2, -2))    

sample = [-2,5,-1,-2]
print(countRangeSum(sample, 2, -2))    
