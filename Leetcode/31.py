
#31. Next Permutation 

def getOrder(data):
    if (len(data) <= 1): 
        raise ValueError("data length shall more than 1")

    p, pp = 1, 1
    order = 0
    for i in range(len(data)-2, -1, -1):
        for j in range(i+1, len(data), 1):
            if (data[j] < data[i]): 
                order += pp        
        p += 1
        pp *= p

    return order    
            
def getData(order, length):
    if (length <= 1): 
        raise ValueError("data length shall more than 1")
    
    data = []
    rem = [ i for i in range(1,length+1,1) ]
    p, pp = length, 1
    for i in range(length): pp *= (i+1)
    for i in range(length, 0, -1):
        pp //= i
        oo = order // pp
        s = rem.pop(oo)
        data.append(s)
        order -= (oo*pp)
    #data.append(rem[0])    
    return data

def nextP(data):
    if (len(data) < 0): return data
    pp = 1
    for i in range(len(data)): pp *= (i+1)
    order = getOrder(data)
    order += 1
    if (order >= pp): order = 0
    #print((data, order))
    return getData(order, len(data))

print(getOrder([1,2,3]))
print(getOrder([1,3,2]))
print(getOrder([2,1,3]))
print(getOrder([2,3,1]))
print(getOrder([3,1,2]))
print(getOrder([3,2,1]))
print("=================")
print(getData(0, 3))
print(getData(1, 3))
print(getData(2, 3))
print(getData(3, 3))
print(getData(4, 3))
print(getData(5, 3))
print("=================")
print(nextP([1,2,3]))
print(nextP([1,3,2]))
print(nextP([2,1,3]))
print(nextP([2,3,1]))
print(nextP([3,1,2]))
print(nextP([3,2,1]))
print("=================")
print(nextP([1,3,2,4]))
print(nextP([4,3,2,1]))
