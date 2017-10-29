
#164. Maximum Gap

seg = 4
maxbits = 16

def maxGap2(data, upper, lower, sbits):

    if (upper >> (sbits + seg)) != (lower >> (sbits + seg)):
        raise Exception('inconsistent upper & lower')

    if (sbits == 0):
        bucket = []
        for i in range(len(data)):
            if (data[i] > upper or data[i] < lower):
                continue
            bucket.append(data[i])

        maxg = 0
        bucket = sorted(bucket)
        for i in range(1,len(bucket),1):
            gap = bucket[i] - bucket[i-1]
            if (gap > maxg): maxg = gap

        #print((1,upper,lower,maxg))  
        return maxg

    count = 1 << seg
    mask = (count - 1) << sbits
    bucket = [ [0,-1,-1] for i in range(count) ]

    for i in range(len(data)):
        if (data[i] > upper or data[i] < lower):
            continue

        slot = (data[i] & mask) >> sbits
        bucket[slot][0] += 1
        if (bucket[slot][1] == -1): bucket[slot][1] = data[i]
        else: 
            if (bucket[slot][1] < data[i]): bucket[slot][1] = data[i]
        if (bucket[slot][2] == -1): bucket[slot][2] = data[i]
        else: 
            if (bucket[slot][2] > data[i]): bucket[slot][2] = data[i]

    maxg = 0
    prev = -1
    for i in range(count):
        if (bucket[i][0] == 0): continue
        if (prev == -1): 
            prev = i
            continue            
        gap = bucket[i][2] - bucket[prev][1]
        if (gap > maxg): maxg = gap
        prev = i

    #print((2,upper,lower,maxg,mask,sbits,bucket))
    for i in range(count):
        if (bucket[i][0] < 2):
            continue

        est_maxg = bucket[i][1] - bucket[i][2] - bucket[i][0] + 2
        if (est_maxg > maxg):
            gap =  maxGap2(data, bucket[i][1], bucket[i][2], sbits-4)
            if (gap > maxg): maxg = gap

    return maxg

def maxGap(data):

    if (len(data) <= 1): return 0

    upper = data[0]
    lower = data[0]
    for i in range(len(data)):
        if (data[i] > upper): upper = data[i]
        if (data[i] < lower): lower = data[i]

    return maxGap2(data, upper, lower, maxbits - seg)

#samples = [1, 2, 3, 20, 21, 200, 201]
#print("{0}=>{1}".format(samples, maxGap(samples)))
samples = [1, 2, 3, 20, 21, 100, 200, 201, 300]
print("{0}=>{1}".format(samples, maxGap(samples)))
#samples = [1, 2, 3, 20, 21, 200, 201, 2000, 2001]
#print("{0}=>{1}".format(samples, maxGap(samples)))