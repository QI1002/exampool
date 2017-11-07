
#480. Sliding Window Median

def slidingMedian(data, k):
    mm = []
    count = len(data)
    for i in range(count-k+1):
        m = sorted(data[i:i+k])
        if ((k & 1) != 0):
            mm.append(m[k//2])
        else:
            mm.append((m[k//2-1], m[k//2]))
    return mm
 
sample = [1,3,-1,-3,5,3,6,7]
print(slidingMedian(sample, 3)) 
