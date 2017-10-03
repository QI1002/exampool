
#140. Word Break II

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

def swap(d, a, b):
    tmp = d[a]
    d[a] = d[b]
    d[b] = tmp

def dictSort(d):
    for i in range(len(d)):
        min = i
        for j in range(i+1,len(d),1):
            if (len(d[min]) > len(d[j])):
                min = j
        swap(d, min, i)

def dictLink(d):
    result = {}
    for i in range(len(d)):
        result[d[i]] = []
        count = len(d[i])
        for j in range(i+1, len(d), 1):
            if (len(d[j]) <= count): continue
            if (d[j][:count] == d[i]):
                derived = False
                for x in result[d[i]]:
                    if (d[j][:len(x)] == x):
                        derived = True
                if (derived == False):
                    result[d[i]].append(d[j])            

    return result

def dictCombine(s, d):
    dictSort(d)
    print(d)
    link = dictLink(d)
    print(link)
    return dictCombineInternal(s, d, link)
    
def dictCombineInternal(s, d, link):

    st = stack()
    st.push(s)
    st.push("")
    result = [] 
    while(not st.isEmpty()):

        dd = d
        r = st.pop()
        ss = st.pop()
        #print((r, ss))

        if (len(ss) == 0): 
            result.append(r) 
            continue

        while(len(dd) > 0):
            y = None
            for x in dd:
                if (ss[:len(x)] == x):           
                    st.push(ss[len(x):])
                    #rr = list(r)
                    #rr.append(x)
                    #st.push(rr)
                    if (len(r) == 0): st.push(x)
                    else: st.push(r + " " + x)
                    y = x
                    break
            if (y == None): break 
            else: dd = link[y]

    return result              
                        
    
dictionary = ["cat", "cats", "and", "sand", "dog", "catsdog"]
print(dictCombine("catsanddog", dictionary))

