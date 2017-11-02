
#352. Data Stream as Disjoint Intervalis

def disjoint(data):
    result = []
    for i in range(len(data)):
        merge = False
        for j in range(len(result)):
            if (data[i] == (result[j][0]-1)):
                result[j][0] = data[i]
                merge = True
            if (data[i] == (result[j][1]+1)):
                result[j][1] = data[i]
                merge = True

        if (merge == False):
            result.append([data[i], data[i]])

    for j in range(len(result)-1,0,-1):
        if (result[j][0] == result[j-1][1]):
            result[j-1][1] = result[j][1]
            result.pop(j)
    
    return result             
 
sample = [1,3,7,2,6]
sample2 = [1]
for i in range(len(sample)):
    print(disjoint(sample[0:i+1]))
