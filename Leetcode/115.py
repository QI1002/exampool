
#115. Distinct Subsequences

def distinctNum(s1, s2):
    count1 = len(s1)
    count2 = len(s2)

    if (count1 < count2): return 0
    if (count1 == count2 and s1 == s2): return 1

    diff = count1 - count2
    result = [tuple([i for i in range(diff)])]
    start = 0
    while(start < len(result)):
        for j in range(1, count1, 1):
            r = result[start] 
            if ((j-1) in r and not j in r):
                l = list(r)
                x = l.index(j-1)
                l.pop(x)
                l.insert(x, j)
                t = tuple(l)
                if (not t in result):
                    result.append(t)
        start += 1

    #print(result)
    hit = 0
    for x in result:
        y = list(s1)  
        for i in range(len(x)-1, -1, -1):
            y.pop(x[i])
        ys = "".join(y)
        if (ys == s2): hit += 1

    return hit
   
s = "rabbbiity"
t = "rabbit"
print(distinctNum(s, t))
