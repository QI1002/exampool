
#315. Count of Smaller Numbers After Self

def countSmaller(data):
    count = len(data)
    result = []
    for i in range(count-1,-1,-1):
        t = data[i]
        c = 0
        for j in range(i+1,count,1):
            if (t > data[j]): c += 1
        result.insert(0, c)
    
    return result
    
sample = [5, 2, 6, 1]
print(countSmaller(sample))