
#259. 3Sum Smaller

def sum3(data, target):
    sum2 = []
    sum2i = []
    for i in range(len(data)):
        for j in range(i+1, len(data), 1):
            s = data[i]+data[j]
            #if (not s in sum2):
            sum2.append(s)
            sum2i.append((i,j))

    temp = sorted(range(len(sum2)), key=lambda x: sum2[x])
    sum2t = []
    sum2it = []
    for i in range(len(temp)):
        sum2t.append(sum2[i])
        sum2it.append(sum2i[i])

    sum2 = sum2t
    sum2i = sum2it
    dsi = sorted(range(len(data)), key=lambda x: data[x])
    
    #print((dsi, sum2, sum2i))

    result = []
    i = len(sum2)-1
    for j in range(len(dsi)):
        jj = dsi[j]
        t = target - data[jj]
        while(i >= 0 and sum2[i] >= t):
            i -= 1

        for k in range(i, -1, -1):
            if (jj >= sum2i[k][0]): continue
            v = data[jj] + sum2[k]
            result.append((v, jj, sum2i[k][0], sum2i[k][1]))

    return result

sample, target = [-2, 0, 1, 3], 2
print("{0}:{1}:{2}".format(sample, target, sum3(sample, target)))
sample, target = [1, 1, 1, 1], 2
print("{0}:{1}:{2}".format(sample, target, sum3(sample, target)))
sample, target = [1, 1, 1, 1], 4
print("{0}:{1}:{2}".format(sample, target, sum3(sample, target)))

