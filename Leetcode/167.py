
#167. Two Sym II- Input array is sorted 

def PairToValue(ss, v):
    result = []
    i = 0
    while (i < len(ss) and ss[i] < v//2): i += 1
    if (i == len(ss)): return result
    if (ss[i] != v//2): i -= 1
    print(i)
    for j in range(0,i+1,1):
        sv = v - ss[j]
        if (sv in ss[i+1:]):
            result.append((ss[j], sv))
    return result

sample = [2, 7, 11, 15]
print("{0}=>{1}".format(sample, PairToValue(sample,9)))
sample = [2, 4, 5, 7, 11, 15]
print("{0}=>{1}".format(sample, PairToValue(sample,9)))
sample = [2, 7, 9, 9, 11, 15]
print("{0}=>{1}".format(sample, PairToValue(sample,18)))

