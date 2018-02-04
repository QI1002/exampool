
#281. Zigzag Iterator

def zigzag(data):
    allens = [ len(x) for x in data ]
    result = []
    while(sum(allens) > 0):
        for i in range(len(allens)):
            if (allens[i] > 0):
                result.append(data[i].pop(0))
                allens[i] -= 1
    return result

data = [[1,2,3],[4,5,6,7],[8,9]]
print("{0}=>{1}".format(data, zigzag(data)))
