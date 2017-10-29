
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
    
def countSmallerMerge(t, s, l, r, k):
    for i in range(l, l+k, 1):
        upper = len(t)-1
        lower = 0
        for j in range(l+k, r+1, 1):            
            if (t[i] == t[j]): 
                s[i] += s[j]
                break

            if (t[i] < t[j]):
                uu = s[i]+s[j]
                if (upper > uu): upper = uu  
            else:
                s[i] += 1
                ll = s[i]+s[j]
                if (lower < ll): lower = ll
                   
            if (upper == lower): 
                s[i] = upper            
                break
            
def countSmaller2(data):
    count = len(data)
    ss = [ 0 for i in range(count) ]
    k = 1
    while(k < count):
        kk = k + k
        for i in range(0, count, kk):
            start = i
            end = count if ((i+kk) > count) else i+kk
            if ((end-start) > k): 
                print((ss, start, end-1, k))
                countSmallerMerge(data, ss, start, end-1, k)               
        k = kk
        
    return ss    
        
sample = [5, 2, 6, 1, 9]
print(countSmaller2(sample))
print(countSmaller(sample))
sample = [5, 2, 6, 1, 9, 4, 0]
print(countSmaller2(sample))
print(countSmaller(sample))
sample = [1, 2, 3, 4, 5, 6, 7]
print(countSmaller2(sample))
print(countSmaller(sample))
sample = [7, 6, 5, 4, 3, 2, 1]
print(countSmaller2(sample))
print(countSmaller(sample))
sample = [7, 1, 1, 1, 1, 1, 1]
print(countSmaller2(sample))
print(countSmaller(sample))