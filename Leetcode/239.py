
#239. Sliding Window Maximum

def slidingMax(data, k):
    result = []
    count = len(data)
    for i in range(count-k+1):
        l = sorted(data[i:i+k])
        result.append(l[-1])

    return result

sample = [1,3,-1,-3,5,3,6,7]
print(slidingMax(sample, 3))    
