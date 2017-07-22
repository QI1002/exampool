

def subset(data):
    if (len(data) == 1):
        result = []
        result.append(data)
        return result
    else:
        first = data[0] 
        result = subset(data[1:])
        more = [[first]]
        #print(str(data) + " " + str(result))  
        for x in result:
            t = list(x)
            t.insert(0, first)
            more.append(t)
    
        result.extend(more)
        return result             
                
print("result={0}".format(subset([1,2,3,4])))                