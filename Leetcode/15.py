
#15. 3Sum

def tripleSum(data):
    ss = []
    dd = []
    result = []
    for i in range(len(data)):
        for j in range(i+1,len(data),1):
            sum = data[i] + data[j]
            if (not sum in ss):
                ss.append(sum)
                dd.append((i,j))

    for i in range(len(ss)):
        s = ss[i]
        d = dd[i]
        j = 0
        while (-s in data[j:]): 
            jj = data[j:].index(-s)
            if ((jj+j) != d[0] and (jj+j) != d[1]):
                t = (data[d[0]],data[d[1]],data[jj+j])
                t = sorted(t)
                if (not t in result): result.append(t)
                break
            j = jj+1

    return result

data = [-1,0,1,2,-1,-4]
print("{0}=>{1}".format(data, tripleSum(data)))
        
