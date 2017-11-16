
#410. split array largest sum 

def greedy(data, mm):
    result = []
    sum = 0
    j = 0

    for i in range(len(data)):
        sum += data[i]
        if (sum > mm):           
            result.append(data[j:i])
            sum = data[i]
            j = i

    if (sum != 0): 
        result.append(data[j:])

    return result

def splitArray(data, m):
    max = 0
    sum = 0
    for x in data: 
        if (max < x): max = x
        sum += x
   
    result = {}
    for s in range(max, sum+1, 1):
        result[s] = greedy(data, s)
        #print("{0}:{1}".format(s, result[s]))
        if (len(result[s]) == m):  return result[s]

    return None

samples = [7, 2, 5, 10, 8]
m = 2
print(splitArray(samples, m))

samples = [1, 2, 3, 4, 5]
m = 3
print(splitArray(samples, m))

