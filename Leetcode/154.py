
#154. Find Minimum in Rotated Sorted Array II

def findMin(data):
    for i in range(1,len(data),1):
        if (data[i] < data[i-1]):
            return data[i]
            
    return data[0]
    
data = [1,2,2,1,1]
print("{0} min is {1}".format(data, findMin(data)))
data = [2,1,1,1,2]
print("{0} min is {1}".format(data, findMin(data)))
data = [1,2,3,4,5]
for i in range(len(data)):
    newdata = data[i:]
    newdata.extend(data[0:i])
    print("{0} min is {1}".format(newdata, findMin(newdata)))

            