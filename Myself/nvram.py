

# new NVRAM flow
# support wild card, don't care support
# support quick search 
# capability to extend demension and factors 
# cache flow to quick seek

class maskSearch:
    def __init__(self, table, spec):
        self.table = table
        self.spec = spec    
        self.tablecode = self.getCodings()
        self.cache = None

    def getCoding(self, entry):
        count = len(self.spec)
        result = []
        for i in range(count):
            cc = self.spec[i]+1
            x = [entry[i]] if type(entry[i]) == int else entry[i]
            c = len(x)
            k = 0
            for j in range(cc):
                if (k < c and x[k] == j):
                    v = 1
                    k += 1
                else:
                    v = 1 if (k < c and x[k] == -1) else 0

                result.append(v)
    
        answer = 0
        for i in range(len(result)):
            if (result[i] == 1):
                answer |= (1<<i)         

        return answer

    def printcode(self, code):
        s = sum(self.spec) + len(self.spec)
        print(format(code, "0"+str(s)+"b"))

    def getCodings(self):
        result = []
        for i in range(len(self.table)):
            c = self.getCoding(self.table[i])
            result.append(c)
            #self.printcode(c)

        return result

    def lookup(self, target):

        code = self.getCoding(target)
        #self.printcode(code)

        if (self.cache != None and self.cache[0] == target):
            return self.cache[1] 

        for i in range(len(self.table)):            
            if ((code & self.tablecode[i]) == code):
                t = self.table[i]
                self.cache = (target, t[len(t)-1])
                return t[len(t)-1]
         
        return None

    def getMemoryComplex(self):
        return (1, len(self.tablecode)) 

    def getCalculateComplex(self):
        return (1, len(self.tablecode)/2.0)

class hashSearch():
    def __init__(self, table, spec):
        self.table = table
        self.extendtable = []
        self.spec = spec
        self.extend()
        self.masks = []
        self.maskhash = []
        self.linkHash()
        self.cache = None

        #print(self.extendtable)
        #print(self.maskhash)
        #print(self.masks)

    def getMask(self, entry):
        result = []
        count = 0
        for i in range(len(self.spec)):
            if (type(entry[i]) == int and entry[i] == -1):
                result.append(1)
                count += 1
            else:
                result.append(0)
 
        answer = 0
        for i in range(len(result)):
            if (result[i] == 1):
                answer |= (1<<i)

        return answer, count

    def printmask(self, mask):
        s = len(self.spec)
        print(format(mask, "0"+str(s)+"b"))

    def getMasks(self, table):
        result = []
        for i in range(len(table)):
            m, c = self.getMask(table[i])
            result.append((c,m))
            #self.printmask(m)

        return result

    def extend(self):
        base = []
        for i in range(len(self.table)):
            entry = self.table[i]
            result = []
            for j in range(len(entry)):
                result = []
                x = [entry[j]] if type(entry[j]) == int else entry[j]
                if (j == 0):
                    result = [[k] for k in x] 
                else:
                    for r in base:
                        for k in x:
                            l = list(r)
                            l.append(k)
                            result.append(l)

                base = result    
    
            self.extendtable.extend(result)
            #print(result)

    def getKey(self, index, mask):
        result = []
        for i in range(len(index)):
            if ((mask & (1<<i)) == 0):
                result.append(index[i])
        return tuple(result)
    
    def linkHash(self):
        maskpairs = self.getMasks(self.extendtable)
        masks = [ k[1] for k in sorted(maskpairs) ]
        #print(masks)
        self.maskhash = {}
        for x in masks:
            if (x not in self.maskhash):
                self.maskhash[x] = {}
                self.masks.append(x)

        for i in range(len(self.extendtable)):
            x = masks[i]
            y = self.extendtable[i]
            v = y.pop()
            key = self.getKey(y, x)
            #print((key,x,v))
            self.maskhash[x][key] = v 
             
    def lookup(self, target): 

        if (self.cache != None and self.cache[0] == target):
            return self.cache[1] 

        for m in self.masks:
            key = self.getKey(target, m)
            if (key in self.maskhash[m]):
                self.cache = (target, self.maskhash[m][key])
                return self.maskhash[m][key]

        return None    

    def getMemoryComplex(self):
        return (len(self.masks), len(self.extendtable)) 

    def getCalculateComplex(self):
        return (len(self.masks)/2.0, 1)

sample_spec = [2, 3, 5, 2, 4] 
sample1 = [[1,2], 0, 1, 2, [3,4], 1]
sample2 = [2, 3, [4,5], 1, 0, 2]
sample3 = [0, 0, -1, [0,1], 1, 3]
sample4 = [-1, -1, 1, 2, 3, 4]

samples = [sample1, sample2, sample3, sample4]
#searchClass = maskSearch
searchClass = hashSearch
search = searchClass(samples, sample_spec) 
print("complext is {0},{1}".format(search.getMemoryComplex(), search.getCalculateComplex()))
 
v = [1,2,1,2,3]
print("lookup {0} and get {1}".format(v, search.lookup(v))) 

v = [1,0,1,2,3]
print("lookup {0} and get {1}".format(v, search.lookup(v))) 


