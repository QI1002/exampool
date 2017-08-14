
def min(data):
    count = len(data)
    m = data[0]
    for i in range(1, count, 1):
        if (m > data[i]):
            m = data[i]
    return m
            
def findMaxSum(data):    
    data.insert(0, 0)
    count = len(data)
    minSum = 0
    minValue = 0
    maxValue = min(data)
    maxStart = 0
    maxEnd = 0
    sum = [0]
    for i in range(1, count, 1):        
        sum.append(data[i] + sum[i-1])            
        v = sum[i] - sum[minSum]
        
        if (maxValue < v):
            maxValue = v
            maxStart = minSum 
            maxEnd = i
            
        if (minValue > sum[i]):
            minValue = sum[i]
            minSum = i
                     
    template.pop(0)        
    return (maxValue, maxStart, maxEnd-1)

template = [2, -8, 3, -2, 4, -10]
m1,m2,m3 = findMaxSum(template)
print("the max sum of {0} is {1} from {2} to {3}".format(template, m1, m2, m3))
template = [2, -8, -3, -2, -4, 10]
m1,m2,m3 = findMaxSum(template)
print("the max sum of {0} is {1} from {2} to {3}".format(template, m1, m2, m3))