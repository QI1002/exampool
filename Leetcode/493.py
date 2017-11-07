
#493. Reverse Pairs

def reversePairs(data):
    count = 0
    for i in range(len(data)):
        for j in range(i+1, len(data), 1):    
            if (data[i] > data[j]*2):
                count += 1

    return count

def reverseMerge(data, s, e, k):
    c = 0
    for i in range(s, s+k, 1):
        for j in range(s+k, e, 1):
            if (data[i] > data[j]*2):
                c += 1
    return c

def reversePairs2(data):
    count = len(data)
    k = 2
    c = 0
    while(k < count):
        kk = k + k
        for i in range(0, count, kk):
            start = i
            end = count if ((i+kk) > count) else i+kk
            if ((end-start) > k):
                c += reverseMerge(data, start, end, k)
                #print((start, end-1, k, c))

        k = kk

    return c

sample = [1,3,2,3,1]
print(reversePairs(sample))
print(reversePairs2(sample))

sample = [2,4,3,5,1]
print(reversePairs(sample))
print(reversePairs2(sample))

