
#488. Zuma Game

class stack:
    def __init__(self):
        self.body = []

    def push(self, data):
        self.body.append(data)

    def pop(self):
        if (len(self.body) == 0):
            return None
        else:
            return self.body.pop()

    def isEmpty(self):
        return True if len(self.body) == 0 else False

def removeStr(s, i):
    l = list(s)
    l.pop(i)
    return "".join(l)

def zuma(data, hands):
    s = stack()
    s.push(hands)
    s.push(data)

    maxh = "" 
    maxl = -1
    while(not s.isEmpty()):
        d = s.pop()
        h = s.pop()
        #print((d,h))

        update = True
        while(update):
            update = False
            select = []
            for i in range(len(d)-2):
                if (d[i] == d[i+1] and d[i] == d[i+2]): 
                    if (not i in select): select.append(i)
                    if (not (i+1) in select): select.append(i+1)
                    if (not (i+2) in select): select.append(i+2)

            for i in range(len(select)-1,-1,-1):
                d = removeStr(d, select[i])
                update = True

        #print(d)
        if (len(d) == 0):
            if (maxl < len(h)): 
                maxl, maxh = len(h), h

        select = []
        for i in range(len(d)-1):
            if (d[i] == d[i+1]): select.append(i) 

        #print(select) 
        update = False
        for i in select:
            if (not d[i] in h): continue

            j = h.index(d[i])
            newh = removeStr(h, j)
            newd = removeStr(d, i+1)
            newd = removeStr(newd, i) 
            update = True

            if (len(newd) == 0):
                if (maxl < len(newh)): 
                    maxl, maxh = len(newh), newh
            else:
                s.push(newh)
                s.push(newd)

        if (update == True): continue

        for i in range(len(d)):
            if (not d[i] in h): continue
            j = h.index(d[i])
            newh = removeStr(h, j)
            if (not d[i] in newh): continue
            j = newh.index(d[i])
            newh = removeStr(newh, j)
            newd = removeStr(d, i)
             
            if (len(newd) == 0):
                if (maxl < len(newh)): 
                    maxl, maxh = len(newh), newh
            else:
                s.push(newh)
                s.push(newd)

    if (maxl == -1): 
        return maxl, maxh

    hh = hands
    for i in range(len(maxh)):
        j = hands.index(maxh[i])
        hh = removeStr(hh, j)
    return len(hands)-maxl, hh
    
print(zuma("WRRBBW", "RB"))
print(zuma("WRRBBW", "RBW"))               
print(zuma("WWRRBBWW", "WRBRW"))        
print(zuma("G","GGGGG"))
print(zuma("RBYYBBRRB","YRBGB"))
