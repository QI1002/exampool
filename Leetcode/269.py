
#269. Alien Dictionary 

def getOrder(less):
    if (len(less) == 0): return ""
    updated = True
    while(updated):
        updated = False
        remove = []
        for i in range(len(less)):
            for j in range(i+1, len(less), 1):
                a, b = less[i]
                x, y = less[j]
                if (a == x and (y, b) in less):
                    remove.append((a,b))
                    updated = True
        for x in remove: less.remove(x) 
        print(less)

    remind = []
    order = ""
    while(True):
        for x in less:
            a = x[0]
            b = x[1]
            if (a in order):
                ai = order.index(a)
                if (b in order):
                    bi = order.index(b)
                    if (bi < ai): raise ValueError("order is inconsistent")
                else:
                    if (ai == (len(order)-1)): order += b
                    else: remind.append(x) 
            else:
                if (b in order):
                    bi = order.index(b)
                    if (bi == 0): order = a + order
                    else: remind.append(x)
                else:
                    if (len(order) == 0):
                        order = a+b
                    else:    
                        remind.append(x)

        #print((order, remind))
        if (len(remind) >= len(less)):
            raise ValueError("ambigous")
        if (len(remind) == 0):
            break
        less = remind
        remind = []

    return order        

def alienDict(data):
    less = []
    for i in range(1, len(data), 1):
        j = 0
        a = data[i-1]
        b = data[i]
        while(j < len(a) and j < len(b) and a[j] == b[j]): 
            j += 1
        if (j >= len(a) or j >= len(b)):
            continue
        if (not (a[j],b[j]) in less):
            less.append((a[j],b[j]))
    #print(less)
    return getOrder(less)

data = ["wrt", "wrf", "er", "ett", "rftt"]
print(alienDict(data))
less = [('a','b'),('b','d'),('c','d'),('b','c'),('d','e')]
print(getOrder(less))
less.insert(0, ('a','e'))
print(getOrder(less))
