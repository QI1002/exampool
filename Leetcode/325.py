
#325. MAximum Size Subarray Sum Equals k

def maxSizeSum(data, k):

    if (len(data) == 0): return 0

    acc = [ 0 for i in range(len(data)+1) ]
    for i in range(1, len(acc)):
        acc[i] = acc[i-1] + data[i-1]

    for d in range(len(data), 0, -1):    
        for j in range(len(data), d-1, -1):
            r = acc[j] - acc[j-d]
            if (r == k): return (d, (j-1, j-d))

    return 0               

given = [1,-1,5,-2,3],3
print("{0}:{1}".format(given, maxSizeSum(*given)))
given = [-2,1,2,1],1
print("{0}:{1}".format(given, maxSizeSum(*given)))
given = [-2,1,2,1],-2
print("{0}:{1}".format(given, maxSizeSum(*given)))
given = [-2,0,2,1],-2
print("{0}:{1}".format(given, maxSizeSum(*given)))


